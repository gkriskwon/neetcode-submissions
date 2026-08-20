# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if not root:
            return result

        q = collections.deque([root])
        
        while q:
            curr_size = len(q)
            curr_level = []
            
            for _ in range(curr_size):
                node = q.popleft()
                curr_level.append(node.val)

                if node.left: 
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            result.append(curr_level)

        return result