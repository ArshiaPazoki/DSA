#!/usr/bin/env python3
import os
import sys
from pathlib import Path
from typing import Iterable, List, Tuple

from pathspec import PathSpec
from pathspec.patterns.gitwildmatch import GitWildMatchPattern


def read_lines(path: Path) -> List[str]:
    if not path or not path.exists():
        return []
    with path.open("r", encoding="utf-8", errors="ignore") as f:
        return [ln.rstrip("\n") for ln in f]


def normalize_rel(p: Path, root: Path) -> str:
    # Always POSIX-style and never prefix with "./"
    return p.resolve().relative_to(root).as_posix()


def scoped_patterns(dir_rel: str, lines: Iterable[str]) -> List[str]:
    """
    Scope .gitignore lines found in directory `dir_rel` so they behave
    exactly like Git:
      - Patterns in a nested .gitignore apply ONLY under that directory.
      - Leading '/' means 'from this .gitignore directory'.
      - No leading '/' means 'any depth under this directory'.
      - Negations '!' keep their negation but are scoped the same way.
    We achieve this by prefixing with the directory path.
    """
    out: List[str] = []
    for raw in lines:
        line = raw.strip()
        if not line or line.startswith("#"):
            continue

        neg = line.startswith("!")
        body = line[1:] if neg else line

        # Git treats trailing spaces literally unless escaped — we keep simple here.
        # Scope to directory containing the .gitignore:
        # - If body starts with '/', it's relative to that directory.
        # - Otherwise it matches at any depth under that directory, so prefix '**/'.
        if dir_rel:
            if body.startswith("/"):
                scoped = f"/{dir_rel}{body}"
            else:
                # e.g. dir_rel/**/pattern
                scoped = f"/{dir_rel}/**/{body}"
        else:
            # At repo root: leave patterns as-is (root semantics are already correct)
            scoped = body if body.startswith("/") else f"**/{body}"

        out.append(("!" + scoped) if neg else scoped)
    return out


def collect_gitignore_patterns(repo_root: Path) -> List[str]:
    """
    Gather patterns from:
      - .gitignore files at every level in the repo
      - .git/info/exclude (if present)
      - Global excludes (~/.config/git/ignore or ~/.gitignore), if present
    We then scope nested .gitignore patterns to their directories.
    """
    all_patterns: List[str] = []
    all_patterns.append("/.git")
    # 1) Per-directory .gitignore (walk the tree, but avoid following ignored dirs later)
    for dirpath, dirnames, filenames in os.walk(repo_root):
        d = Path(dirpath)
        rel = "" if d == repo_root else normalize_rel(d, repo_root)
        gi = d / ".gitignore"
        if gi.exists():
            lines = read_lines(gi)
            all_patterns.extend(scoped_patterns(rel, lines))

    # 2) .git/info/exclude (root-scoped)
    info_exclude = repo_root / ".git" / "info" / "exclude"
    if info_exclude.exists():
        all_patterns.extend(scoped_patterns("", read_lines(info_exclude)))

    # 3) Global excludes (common locations)
    home = Path.home()
    for global_candidate in [
        home / ".config" / "git" / "ignore",
        home / ".gitignore",
    ]:
        if global_candidate.exists():
            all_patterns.extend(scoped_patterns("", read_lines(global_candidate)))

    return all_patterns


def build_spec(repo_root: Path) -> PathSpec:
    patterns = collect_gitignore_patterns(repo_root)
    # If no patterns were found, use an empty spec
    return PathSpec.from_lines(GitWildMatchPattern, patterns)


def list_children(base: Path) -> Tuple[List[Path], List[Path]]:
    """Return (dirs, files) sorted case-insensitively."""
    dirs, files = [], []
    for e in base.iterdir():
        (dirs if e.is_dir() else files).append(e)
    key = lambda p: p.name.lower()
    return sorted(dirs, key=key), sorted(files, key=key)


def print_tree(
    root: Path,
    repo_root: Path,
    spec: PathSpec,
    prefix: str = "",
):
    dirs, files = list_children(root)

    def visible(paths: List[Path]) -> List[Path]:
        out = []
        for p in paths:
            rel = normalize_rel(p, repo_root)
            # PathSpec.match_file expects POSIX-ish path strings (we provide rel)
            # If a path is matched by a negation, PathSpec handles order/negation rules.
            if not spec.match_file(rel):
                out.append(p)
        return out

    dirs = visible(dirs)
    files = visible(files)
    entries = dirs + files

    for i, entry in enumerate(entries):
        connector = "└── " if i == len(entries) - 1 else "├── "
        print(prefix + connector + entry.name)
        if entry.is_dir():
            extension = "    " if i == len(entries) - 1 else "│   "
            print_tree(entry, repo_root, spec, prefix + extension)


def find_repo_root(start: Path) -> Path:
    """
    Try to locate the repo root (directory that contains the top-level .git directory
    or the first directory up that has a .gitignore). If not found, fall back to `start`.
    """
    cur = start.resolve()
    last = None
    while cur != last:
        if (cur / ".git").exists() or (cur / ".gitignore").exists():
            return cur
        last, cur = cur, cur.parent
    return start.resolve()


def main():
    start = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    start = start.resolve()

    repo_root = find_repo_root(start)
    spec = build_spec(repo_root)

    # Show the tree starting at `start`, respecting ignores collected from `repo_root`
    print(start.name)
    print_tree(start, repo_root, spec, "")


if __name__ == "__main__":
    main()
