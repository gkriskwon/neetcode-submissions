class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        ROWS = len(grid)
        COLS = len(grid[0])
        islands = 0

        def dfs(row, col):
            # out of bounds? 
            # visited? 
            # water? 
            if 0 > row or ROWS <= row or 0 > col or COLS <= col or (row, col) in visited or grid[row][col] == '0':
                return

            visited.add((row, col))

            dfs(row + 1, col)
            dfs(row, col + 1)
            dfs(row - 1, col)
            dfs(row, col - 1)


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r, c) not in visited:
                    dfs(r, c)
                    islands += 1

        return islands


            
