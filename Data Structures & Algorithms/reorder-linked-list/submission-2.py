# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1. 중간지점 찾기 
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. 반쪽 뒤집기 
        second = slow.next
        prev = None
        slow.next = None

        while second:
            tmp = second.next   # 다음노드 저장
            second.next = prev  # 다음노드 = 이전노드  
            prev = second       # 이전노드 업데이트 (현재로)
            second = tmp        # 현재 노드 다음으로 이동 

        # 두 리스트 병합 
        first = head
        second = prev

        while second: # 무조건 second가 같거나 적음
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2



        