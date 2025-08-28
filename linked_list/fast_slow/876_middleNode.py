from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    head = None
    def __init__(self, values:List[int]):
        self.head = ListNode(values[0])
        current = self.head
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next

class Solution:
    def middleNode(self, head:Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
            

if __name__ == '__main__':
    values = [1,2,3,4,5]
    print(Solution().middleNode(LinkedList(values).head))

