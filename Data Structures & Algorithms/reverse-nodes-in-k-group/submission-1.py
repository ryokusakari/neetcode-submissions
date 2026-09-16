# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        finalhead = pointer = head
        stack = []

        i = 0
        while pointer:
            if i % k == 0:
                stack.append([pointer])
                finalhead = pointer
            else:
                stack[i//k].append(pointer)
            pointer = pointer.next
            i += 1

        prevhead = None
        if i%k != 0:
            prevhead = finalhead
            stack.pop()

        while stack:
            current_stack = stack.pop()
            current_head = current_stack.pop()
            pointer = current_head
            while current_stack:
                pointer.next = current_stack.pop()
                pointer = pointer.next
            pointer.next = prevhead
            prevhead = current_head
        
        return prevhead
        

        

            


        





        