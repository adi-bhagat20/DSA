class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        seen = set()
        
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                
                if val != ".":
                    # Unique identifiers for row, column, and 3x3 sub-box
                    row_id = f"row {i} has {val}"
                    col_id = f"col {j} has {val}"
                    box_id = f"box {i // 3}-{j // 3} has {val}"
                    
                    # If any of these identifiers already exist, it's an invalid Sudoku
                    if row_id in seen or col_id in seen or box_id in seen:
                        return False
                    
                    # Add them to the set
                    seen.update([row_id, col_id, box_id])
                    
        return True
