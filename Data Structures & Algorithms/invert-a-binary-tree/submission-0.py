# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert_branch(current):
            if current is None:
                return None
            
            left = invert_branch(current.left)
            right = invert_branch(current.right)
            current.right = left
            current.left = right

            return current

        return invert_branch(root)