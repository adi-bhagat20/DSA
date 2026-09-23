class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        seen = set()
        
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                
                if val != ".":
                    # Unique identifiers using tuples instead of lists
                    # Adding a tag like "row", "col", or "box" keeps them distinct
                    row = ("row", i, val)
                    col = ("col", j, val)
                    box = ("box", i // 3, j // 3, val)
                    
                    # If any of these identifiers already exist, it's an invalid Sudoku
                    if row in seen or col in seen or box in seen:
                        return False
                    
                    # Add them to the set
                    seen.update([row, col, box])
                    
        return True
