class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj_list = defaultdict(list)

        for u, v, w in edges:
            adj_list[u].append((v, w))

        shortest = {}
        min_heap = [[0, src]]
        
        while min_heap:
            current_dist, current_node = heapq.heappop(min_heap)
            if current_node in shortest:
                continue

            shortest[current_node] = current_dist

            for neighbor, weight in adj_list[current_node]:
                if neighbor not in shortest:
                    new_dist = current_dist + weight
                    heapq.heappush(min_heap, (new_dist, neighbor))

        for i in range(n):
            if i not in shortest:
                shortest[i] = -1

        return shortest

