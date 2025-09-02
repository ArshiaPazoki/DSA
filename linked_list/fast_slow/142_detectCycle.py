from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next


class Solution:
    def detectCycle(self, head:Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None
    
# build 3->2->0->-4, with tail pointing to node '2'
n3 = ListNode(-4)
n2 = ListNode(0, n3)
n1 = ListNode(2, n2)
h  = ListNode(3, n1)
n3.next = n1  # cycle starts at n1 (value 2)

# run
start = Solution().detectCycle(h)
assert start is n1  # same object identity
print(start.val)    # 2