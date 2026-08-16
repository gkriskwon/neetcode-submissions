class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        max_row = len(grid)
        max_col = len(grid[0])
        end = (max_row - 1, max_col - 1)

        visited = defaultdict(bool)

        def find_path(row, col):
            nonlocal end
            if row < 0 or row >= max_row or col < 0 or col >= max_col:
                return 0
            if visited[(row, col)]:
                return 0
            if grid[row][col] == 1:
                return 0
            if (row, col) == end:
                return 1
            visited[(row, col)] = True
            num_path = 0
            # up
            num_path += find_path(row - 1, col)
            # down
            num_path += find_path(row + 1, col)
            # left
            num_path += find_path(row, col - 1)
            # right
            num_path += find_path(row, col + 1)
            visited[(row, col)] = False
            
            return num_path

        return find_path(0, 0)

