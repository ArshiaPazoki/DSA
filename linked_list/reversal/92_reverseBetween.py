from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        prehead = ListNode(0)
        prehead.next = head
        prev = prehead
        for _ in range(left-1):
            prev = prev.next
        curr = prev.next
        for _ in range(right - left):
            next = curr.next
            curr.next = next.next
            next.next = prev.next
            prev.next = next
        return prehead.next


if __name__ == '__main__':
    head = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
    left = 2
    right = 4
    Solution().reverseBetween(head, left, right)