# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def is_balanced(current):
            if current is None:
                return (True, 0)
            left_bal, left_len = is_balanced(current.left)
            right_bal, right_len = is_balanced(current.right)

            is_bal = (
                left_bal and right_bal and abs(left_len - right_len) <= 1
            )

            current_height = 1 + max(left_len, right_len)
            return is_bal, current_height

        return is_balanced(root)[0]
