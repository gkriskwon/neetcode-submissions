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
            
        oldToNew = {}

        def cloneNode(curr):
            # 이미 복제된 노드라면 저장된 복제본을 반환
            if curr in oldToNew:
                return oldToNew[curr]

            # 1. 현재 노드 자체를 복제
            copy = Node(curr.val)
            oldToNew[curr] = copy

            # 2. 이웃들을 재귀적으로 복제해서 내 이웃 리스트에 추가
            for nei in curr.neighbors:
                # "내 이웃 노드를 복제(cloneNode)해와서 연결해줘"
                copy.neighbors.append(cloneNode(nei))
            
            return copy

        return cloneNode(node)