class Solution:

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # start from 0 instead of INF
        INF = 2147483647
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        

        q = collections.deque([])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
                    # explore land from the chest till reach water

        while q:
            r, c = q.popleft()
        
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < ROWS 
                    and 0 <= nc < COLS
                    and (nr, nc) not in visited
                    and grid[nr][nc] == INF
                ):
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr, nc))
                    


        return 


