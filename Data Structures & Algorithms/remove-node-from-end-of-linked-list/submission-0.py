# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        dummy_head.next = pointer = head
        counter = 0
        while pointer.next:
            pointer = pointer.next
            counter += 1

        pointer = dummy_head
        for _ in range(counter-n+1):
            pointer = pointer.next
        connector = None if n == 1 else pointer.next.next 
        pointer.next = connector
        
        return dummy_head.next

