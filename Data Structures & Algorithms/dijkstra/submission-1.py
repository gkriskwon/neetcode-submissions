class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj_list = defaultdict(list)

        for u, v, w in edges:
            adj_list[u].append((v, w))

        shortest_dist_of = {src: 0} # node: shortest dist
        short_dist_pq = [[0, src]]
        shortest_dist_of[src] = 0
        visited = set()

        while short_dist_pq:
            cur_dist, cur_node = heapq.heappop(short_dist_pq)
            if cur_node in visited:
                continue
            visited.add(cur_node)

            for neighbor, weight in adj_list[cur_node]:
                new_dist = shortest_dist_of[cur_node] + weight
                if neighbor not in shortest_dist_of or new_dist < shortest_dist_of[neighbor]:
                    shortest_dist_of[neighbor] = new_dist
                    heapq.heappush(short_dist_pq, (new_dist, neighbor))

        for i in range(n):
            if i not in shortest_dist_of:
                shortest_dist_of[i] = -1

        return shortest_dist_of

