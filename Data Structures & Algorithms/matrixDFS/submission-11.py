class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        visited = set()

        def dfs(row, col):
            if (
                row < 0 or row >= ROWS or col < 0 or col >= COLS 
                or grid[row][col] == 1 or (row, col) in visited
            ):
                return 0

            if row == ROWS - 1 and col == COLS - 1:
                return 1

            visited.add((row, col))
            num_path = 0
            # up
            num_path += dfs(row - 1, col)
            # down
            num_path += dfs(row + 1, col)
            # left
            num_path += dfs(row, col - 1)
            # right
            num_path += dfs(row, col + 1)
            visited.remove((row, col))
            
            return num_path

        return dfs(0, 0)

