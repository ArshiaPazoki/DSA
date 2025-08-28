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
        count = 1
        current = head
        while current.next:
            count += 1
            current = current.next
        answer = (count/2) if count%2==0 else (count -1)/2
        current = head
        while answer > 0:
            current = current.next
            answer -= 1
        return current
            

if __name__ == '__main__':
    values = [1,2,3,4,5]
    print(Solution().middleNode(LinkedList(values).head))

