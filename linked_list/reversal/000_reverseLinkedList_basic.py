"""
Algorithm:
    Reverse a Linked List

A.K.A:
- Linked List Reversal
- Reverse Singly Linked List
- Reverse Iteratively / Recursively

Complexity:
- Time: O(n)   (must visit each node once)
- Space:
    Iterative: O(1)
    Recursive: O(n) (due to call stack)

What it solves (one-liner):
    Transform a linked list so that its direction is reversed:
        head → ... → tail  becomes  tail → ... → head.

Intuition:
    Each node has a pointer to "next". To reverse, we flip that pointer.
        We must keep track of:
            - current node
            - previous node (what it should now point to)
            - next node (to not lose the chain while flipping)

Step-by-step (iterative):
    1. Initialize: prev = None, curr = head
    2. While curr != None:
        a. Save next_node = curr.next
        b. Redirect curr.next → prev
        c. Move prev = curr
        d. Move curr = next_node
    3. At end, prev is new head

Step-by-step (recursive):
    Base case: if node is None or node.next is None → return node.
    Recursive case:
        - new_head = reverse(node.next)
        - node.next.next = node
        - node.next = None
        - return new_head

Correctness (sketch):
    Invariant: all nodes behind `prev` already reversed.
    Loop maintains invariant by one-step pointer flip.
    Termination: when curr=None, prev points to new head.
    For recursion: base (0/1 node) is trivially reversed; induction flips the edge to the current head.

Edge cases:
    - Empty list (head=None) → return None
    - Single element list → same node returned
    - Very long list → recursion may hit recursion depth

Usage:
    - Theoretical: 
        - Basis for many linked list problems (palindrome, reorder, k-group reversal, cycle check).
        - Classic pointer manipulation practice.
    - Real-world: 
        - Reversing sequences in memory-efficient data streams.
        - Undo stacks, persistent data structure transformations.

Pitfalls:
    - Forgetting to store `next_node` before re-linking.
    - Losing reference to list.
    - Returning wrong pointer (should return `prev`).
    - Using recursion on very deep lists can raise RecursionError in Python.

Practice:
    - LeetCode 206. Reverse Linked List
    - LeetCode 92. Reverse Linked List II
    - LeetCode 25. Reverse Nodes in k-Group
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Iterable, List

# Linked List Node definition + Utilities

@dataclass(slots=True)
class ListNode:
    val: int = 0
    next: Optional["ListNode"] = None

    def __iter__(self):
        node = self
        while node:
            yield node.val
            node = node.next

    def __repr__(self) -> str:
        return f"ListNode({self.val})"


def build_linked_list(values: Iterable[int]) -> Optional[ListNode]:
    """
    Build a singly linked list from an iterable of ints.
    Returns the head node (or None if empty).
    """
    head: Optional[ListNode] = None
    tail: Optional[ListNode] = None
    for v in values:
        n = ListNode(v)
        if head is None:
            head = tail = n
        else:
            assert tail is not None
            tail.next = n
            tail = n
    return head


def to_list(head: Optional[ListNode]) -> List[int]:
    """Convert a linked list to a Python list of ints."""
    out: List[int] = []
    node = head
    while node:
        out.append(node.val)
        node = node.next
    return out


def print_list(head: Optional[ListNode]) -> None:
    """Pretty-print a linked list (debug utility)."""
    parts: List[str] = []
    node = head
    while node:
        parts.append(str(node.val))
        node = node.next
    parts.append("None")
    print(" -> ".join(parts))


# Iterative version (O(n) time, O(1) extra space)

def reverse_list_iterative(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Reverse a singly linked list iteratively.

    Args:
        head: The head of the list.

    Returns:
        The new head after reversal.

    Complexity:
        Time: O(n), Space: O(1).
    """
    prev: Optional[ListNode] = None
    curr: Optional[ListNode] = head
    while curr is not None:
        nxt = curr.next        # save next
        curr.next = prev       # flip pointer
        prev = curr            # advance prev
        curr = nxt             # advance curr
    return prev  # new head


# Recursive version (O(n) time, O(n) call stack)

def reverse_list_recursive(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Reverse a singly linked list recursively.

    WARNING: Python recursion depth (~1000 by default) may limit very long lists.

    Args:
        head: The head of the list.

    Returns:
        The new head after reversal.

    Complexity:
        Time: O(n), Space: O(n) due to recursion stack.
    """
    if head is None or head.next is None:
        return head
    new_head = reverse_list_recursive(head.next)
    head.next.next = head
    head.next = None
    return new_head


# Example Usage & Minimal Tests

if __name__ == "__main__":
    # Build list: 1 -> 2 -> 3 -> None
    head = build_linked_list([1, 2, 3])

    # Reverse iteratively
    rev = reverse_list_iterative(head)
    print_list(rev)  # 3 -> 2 -> 1 -> None
    assert to_list(rev) == [3, 2, 1]

    # Reverse back using recursion
    rev_back = reverse_list_recursive(rev)
    print_list(rev_back)  # 1 -> 2 -> 3 -> None
    assert to_list(rev_back) == [1, 2, 3]

    # Edge cases
    assert reverse_list_iterative(None) is None  # empty
    single = build_linked_list([42])
    assert to_list(reverse_list_iterative(single)) == [42]

    print("All sanity checks passed ✅")
