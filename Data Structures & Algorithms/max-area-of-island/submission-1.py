class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        visited = set()

        area = 0

        def find_area(row, col) -> int: # return area
            q = collections.deque([(row, col)])
            visited.add((row, col))
            size = 1

            while q:
                r, c = q.popleft()
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < ROWS
                        and 0 <= nc < COLS 
                        and (nr, nc) not in visited
                        and grid[nr][nc] == 1
                    ):
                        visited.add((nr, nc))
                        q.append((nr, nc))
                        size += 1

            return size

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    area = max(area, find_area(r, c))

        return area
                    


