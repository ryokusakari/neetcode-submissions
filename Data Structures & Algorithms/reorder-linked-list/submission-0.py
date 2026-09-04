# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        stack = []
        dummy_head = ListNode(0)
        pointer = head

        while pointer.next:
            stack.append(pointer)
            pointer = pointer.next
        stack.append(pointer)
        
        l,r = 0,len(stack)-1
        pointer = dummy_head

        while l<r:
            pointer.next = stack[l]
            pointer.next.next = stack[r]
            pointer = pointer.next.next
            l += 1
            r -= 1
            if l == r:
                pointer.next = stack[l]
                pointer = pointer.next
                break
        
        pointer.next = None
        return pointer.next
        