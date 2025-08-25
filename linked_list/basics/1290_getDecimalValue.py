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
    def getDecimalValue(self, head:Optional[ListNode]) -> int:
        answer = 0
        current = head
        while current:
            answer = (answer << 1) | current.val
            current = current.next
        return answer
            

if __name__ == '__main__':
    values = [1,0,1,0]
    print(Solution().getDecimalValue(LinkedList(values).head))

