# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(0)
        pointer = result
        retained_digit = 0

        while l1 or l2:
            if l1 and l2:
                digit_sum = l1.val + l2.val + retained_digit
                l1 = l1.next
                l2 = l2.next
            elif retained_digit == 1:
                value = l1.val if l1 else l2.val
                digit_sum = value + retained_digit
                if l1:
                    l1 = l1.next
                else:
                    l2 = l2.next
            else:
                pointer.next = l1 if l1 else l2
                break

            value = digit_sum % 10
            retained_digit = digit_sum // 10
            
            pointer.next = ListNode(value)
            pointer = pointer.next
        
        if retained_digit == 1:
            pointer.next = ListNode(1)
        
        return result.next
            



            
