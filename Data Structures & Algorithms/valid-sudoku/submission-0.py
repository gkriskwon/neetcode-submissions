class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_sets = defaultdict(set)
        col_sets = defaultdict(set)
        box_sets = defaultdict(set)
        
        # check row for duplicate
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue

                if val in row_sets[r]:
                    return False
                if val in col_sets[c]:
                    return False
                box_coord = (r // 3, c // 3)
                if val in box_sets[box_coord]:
                    return False
                
                row_sets[r].add(val)
                col_sets[c].add(val)
                box_sets[box_coord].add(val)

        return True
