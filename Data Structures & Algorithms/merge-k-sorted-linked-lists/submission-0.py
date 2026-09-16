# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        while len(lists) > 1:
            for i in range(0, len(lists), 2):

                dummy_head = ListNode(0)
                pointer = dummy_head
                list1 = lists[i]
                list2 = lists[i+1] if (i+1) < len(lists) else None

                while list1 and list2:
                    val1, val2 = list1.val, list2.val
                    pointer.next = list1 if val1 <= val2 else list2
                    list1 = list1.next if val1 <= val2 else list1
                    list2 = list2.next if val1 > val2 else list2
                    pointer = pointer.next

                pointer.next = list1 if list1 else list2
                lists[i//2] = dummy_head.next
                
            lists = lists[:i//2+1]
        
        return lists[0]





