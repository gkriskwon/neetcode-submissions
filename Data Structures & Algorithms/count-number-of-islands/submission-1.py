
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        ROWS = len(grid)
        COLS = len(grid[0])
        islands = 0

        def bfs(row, col):
            q = collections.deque([(row, col)])
            visited.add((row, col))

            while q:
                r, c = q.popleft()
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visited and grid[nr][nc] == '1':
                        visited.add((nr, nc))
                        q.append((nr, nc))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1

        return islands


            
