# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        result  = ListNode()
        current = head

        while current:
            temp = current.next
            current.next = result.next
            result.next = current
            current = temp

        return result.next
            
            