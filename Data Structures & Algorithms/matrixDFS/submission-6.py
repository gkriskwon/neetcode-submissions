class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        rows= len(grid)
        cols = len(grid[0])

        if grid[0][0] == 1 or grid[rows - 1][cols - 1] == 1:
            return 0

        target = (rows - 1, cols - 1)
        visited = set()

        def dfs(row, col):
            nonlocal target
            if (row, col) == target:
                return 1
            
            num_path = 0
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                next_row, next_col = row + dr, col + dc 
                if (
                    (next_row, next_col) not in visited
                    and 0 <= next_row < rows
                    and 0 <= next_col < cols
                    and grid[next_row][next_col] != 1
                ):
                    visited.add((next_row, next_col))
                    num_path += dfs(next_row, next_col)
                    visited.remove((next_row, next_col))
                    
            return num_path

        visited.add((0, 0))
        return dfs(0, 0)