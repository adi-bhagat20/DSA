class Solution:
    def valid_rows(self , arr):
        for i in range(9):
            setr = set()
            for j in range(9):
                if arr[i][j] != ".":
                    if arr[i][j] in setr:
                        return False
                    else:
                        setr.add(arr[i][j])
        
        return  True

    def valid_cols(self , arr):
        j = 0
        while j < 9:
            setc = set()
            for i in range(9):
                if arr[i][j] != ".":
                    if arr[i][j] in setc:
                        return False
                    else:
                        setc.add(arr[i][j])
            
            j+=1
        return True

    def valid_boxs(self , arr):
        box1 = set()
        box2 = set()
        box3 = set()
        for i in range(9):
            if i % 3 == 0:
                box1.clear()
                box2.clear()
                box3.clear()
            
            for j in range(0 , 3):
                if arr[i][j] != '.':
                    if arr[i][j] in box1:
                        return False
                    else:
                        box1.add(arr[i][j])
                
            for j in range(3 , 6):
                if arr[i][j] != '.':
                    if arr[i][j] in box2:
                        return False
                    else:
                        box2.add(arr[i][j])

            for j in range(6 , 9):
                if arr[i][j] != '.':
                    if arr[i][j] in box3:
                        return False
                    else:
                        box3.add(arr[i][j])
        return True

    def isValidSudoku(self, board: list[list[str]]) -> bool:
        if self.valid_rows(board) and self.valid_cols(board) and self.valid_boxs(board):
            return True
        return False