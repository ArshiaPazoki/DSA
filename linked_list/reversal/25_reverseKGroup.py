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
    def has_k_nodes(self, head: Optional[ListNode], k: int) -> bool:
        current = head
        for _ in range(k):
            if not current:
                return False
            current = current.next
        return True
    
    def reverse_k_nodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        perv = None
        curr = head
        for _ in range(k):
            next_temp = curr.next
            curr.next = perv
            perv = curr
            curr = next_temp
        return perv,curr

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1 or not head:
            return head
        dummy = ListNode(0)
        dummy.next = head
        perv = dummy
        while self.has_k_nodes(perv.next, k):
            group_head = perv.next
            new_head, next_group = self.reverse_k_nodes(group_head, k)
            perv.next = new_head
            group_head.next = next_group
            perv = group_head
        return dummy.next

if __name__ == '__main__':
    values = [1, 2, 3, 4, 5]
    k = 2
    ll = LinkedList(values)
    solution = Solution()
    new_head = solution.reverseKGroup(ll.head, k)

    result = []
    curr = new_head
    while curr:
        result.append(curr.val)
        curr = curr.next
    print(result)