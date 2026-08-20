# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = 0

        # Every node check left + right 

        def find_diameter(current):
            nonlocal result
            if current is None:
                return 0
            
            left_len = find_diameter(current.left)
            right_len = find_diameter(current.right)

            # Every node check left + right
            result = max(result, left_len + right_len)


            return max(left_len, right_len) + 1

        result = max(find_diameter(root) - 1, result)

        return result