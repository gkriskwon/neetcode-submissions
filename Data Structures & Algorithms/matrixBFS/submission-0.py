class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        if grid[0][0] == 1 or grid[rows - 1][cols - 1] == 1:
            return -1

        q = collections.deque([(0, 0, 0)])
        visited = {(0, 0)}

        target_r = rows - 1
        target_c = cols - 1

        while q:
            r, c, dist = q.popleft()
            if r == target_r and c == target_c :
                return dist 

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and grid[nr][nc] == 0:
                    visited.add((nr, nc))
                    q.append((nr, nc, dist + 1))

        return -1

            
