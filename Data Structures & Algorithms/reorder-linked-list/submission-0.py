# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle
        fast = head
        mid = head

        while fast != None and fast.next != None:
            fast = fast.next.next
            mid = mid.next

        # found mid
        # 뒤집는법
        prev = None
        curr = mid.next
        mid.next = None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        first = head
        second = prev

        while first and second:
            next_node1 = first.next
            next_node2 = second.next
            first.next = second
            second.next = next_node1
            first = next_node1
            second = next_node2


