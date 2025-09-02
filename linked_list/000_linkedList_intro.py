"""
Algorithm / Data Structure:
    Linked List (Singly & Doubly)

A.K.A:
- Singly Linked List (SLL)
- Doubly Linked List (DLL)
- Circular Linked List (CLL)

Complexity:
    Lookup by index: O(n)
    Search by value: O(n)
    Insert at head: O(1)
    Insert at tail: O(1) with tail pointer, else O(n)
    Delete at head: O(1)
    Delete at tail: O(n) (SLL), O(1) (DLL with tail pointer)
    Space: O(n) for nodes (+ overhead for pointers)

What it solves (one-liner):
    Dynamic memory-efficient structure for sequential data 
    where insertions/deletions are frequent and random access is not required.

Intuition:
    An array stores elements contiguously → resizing & insertions are costly.
    A linked list stores elements in nodes, each pointing to the next (and/or previous).
    This allows efficient structural modifications but sacrifices direct indexing.

Types:
    1. Singly Linked List: node points only forward
    2. Doubly Linked List: node points forward & backward
    3. Circular Linked List: last node links back to head

Step-by-step (basic operations on SLL):
    Insert at head:
        1. new_node.next = head
        2. head = new_node
    Insert at tail:
        1. Traverse until tail
        2. tail.next = new_node
    Delete head:
        1. head = head.next
    Delete by value:
        1. Traverse until node before target
        2. node.next = node.next.next
    Search:
        Traverse until val == target or None

Correctness (sketch):
    Each operation preserves the invariant: 
        list = chain of nodes ending in None (or back to head in circular).
    Insert/delete rewire at most 2 pointers → structure remains valid.

Edge cases:
    - Empty list
    - Single element list
    - Deleting head/tail
    - Handling None safely

Usage:
    - Theoretical:
        - Foundation of stacks, queues, hash chains, adjacency lists in graphs.
    - Real-world:
        - Music/playlist navigation
        - Undo/redo systems
        - Memory allocators (free lists)
        - Browser history

Pitfalls:
    - Losing reference to head during modification
    - Memory overhead (extra pointers vs arrays)
    - Poor cache locality (nodes scattered in memory)
    - Recursive implementations may hit recursion depth

Practice (LeetCode — sorted by difficulty, then by problem #):
    EASY:
        - 21.  Merge Two Sorted Lists
        - 83.  Remove Duplicates from Sorted List
        - 141. Linked List Cycle
        - 160. Intersection of Two Linked Lists
        - 203. Remove Linked List Elements
        - 206. Reverse Linked List
        - 234. Palindrome Linked List
        - 237. Delete Node in a Linked List
        - 876. Middle of the Linked List
        - 1290. Convert Binary Number in a Linked List to Integer

    MEDIUM:
        - 2.    Add Two Numbers
        - 19.   Remove Nth Node From End of List
        - 24.   Swap Nodes in Pairs
        - 61.   Rotate List
        - 82.   Remove Duplicates from Sorted List II
        - 86.   Partition List
        - 92.   Reverse Linked List II
        - 109.  Convert Sorted List to Binary Search Tree
        - 138.  Copy List with Random Pointer
        - 143.  Reorder List
        - 147.  Insertion Sort List
        - 148.  Sort List
        - 328.  Odd Even Linked List
        - 369.  Plus One Linked List
        - 430.  Flatten a Multilevel Doubly Linked List
        - 445.  Add Two Numbers II
        - 707.  Design Linked List
        - 708.  Insert into a Sorted Circular Linked List
        - 725.  Split Linked List in Parts
        - 817.  Linked List Components
        - 1019. Next Greater Node In Linked List
        - 1171. Remove Zero Sum Consecutive Nodes from Linked List
        - 1669. Merge In Between Linked Lists
        - 1721. Swapping Nodes in a Linked List
        - 2181. Merge Nodes in Between Zeros
        - 2487. Remove Nodes From Linked List
        - 2807. Insert Greatest Common Divisors in Linked List
        - 2816. Double a Number Represented as a Linked List
        - 3217. Delete Nodes From Linked List Present in Array

    HARD:
        - 23.   Merge k Sorted Lists
        - 25.   Reverse Nodes in k-Group
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Iterable, List

# Singly Linked List Node
@dataclass(slots=True)
class ListNode:
    val: int
    next: Optional["ListNode"] = None

    def __iter__(self):
        node = self
        while node:
            yield node.val
            node = node.next

    def __repr__(self) -> str:
        return f"ListNode({self.val})"
    
# Doubly Linked List Node
@dataclass(slots=True)
class DListNode:
    val: int
    prev: Optional["DListNode"] = None
    next: Optional["DListNode"] = None

    def __repr__(self) -> str:
        return f"DListNode({self.val})"
    
# Linked List Utilities (for SLL)
def build_linked_list(values: Iterable[int]) -> Optional[ListNode]:
    head: Optional[ListNode] = None
    tail: Optional[ListNode] = None
    for v in values:
        n = ListNode(v)
        if not head:
            head = tail = n
        else:
            assert tail is not None
            tail.next = n
            tail = n
    return head


def to_list(head: Optional[ListNode]) -> List[int]:
    out: List[int] = []
    while head:
        out.append(head.val)
        head = head.next
    return out


def print_list(head: Optional[ListNode]) -> None:
    parts: List[str] = []
    while head:
        parts.append(str(head.val))
        head = head.next
    parts.append("None")
    print(" -> ".join(parts))


# Example Usage
if __name__ == "__main__":
    # Build linked list [1, 2, 3]
    head = build_linked_list([1, 2, 3])
    print("Initial list:")
    print_list(head)  # 1 -> 2 -> 3 -> None

    # Insert at head (4)
    new_head = ListNode(4, next=head)
    print("After inserting 4 at head:")
    print_list(new_head)  # 4 -> 1 -> 2 -> 3 -> None

    # Delete head (4)
    new_head = new_head.next
    print("After deleting head (4):")
    print_list(new_head)  # 1 -> 2 -> 3 -> None

    # Convert to Python list
    print("As Python list:", to_list(new_head))  # [1, 2, 3]