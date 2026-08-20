# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        c = result
        c1 = list1
        c2 = list2
        
        while c1 and c2:
            if c1.val < c2.val:
                # c1 to c
                c.next = c1
                c1 = c1.next
            else:
                # c2 to c
                c.next = c2
                c2 = c2.next
            
            c = c.next

        if c1:
            c.next = c1
        if c2:
            c.next = c2

        return result.next
