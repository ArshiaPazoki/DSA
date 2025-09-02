from __future__ import annotations

from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        perv = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = perv
            perv = curr
            curr = next_node
        return perv

if __name__ == '__main__':
    head = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
    print(Solution().reverseList(head).val)


