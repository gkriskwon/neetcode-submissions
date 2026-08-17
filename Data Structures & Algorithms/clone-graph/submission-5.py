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
        copies = {node: Node(node.val)}

        while q:
            c_node = q.popleft()
            for neighbor in c_node.neighbors:
                if neighbor not in copies:
                    copy = Node(neighbor.val)
                    copies[neighbor] = copy
                    q.append(neighbor) # its neighbors will iterated later
                
                copies[c_node].neighbors.append(copies[neighbor])

        return copies[node]
