"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        q = collections.deque([node])
        old_new = {node: Node(node.val)}

        while q:
            c_node = q.popleft()
            for neighbor in c_node.neighbors:
                if neighbor not in old_new:
                    old_new[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
                old_new[c_node].neighbors.append(old_new[neighbor])

        return old_new[node]
