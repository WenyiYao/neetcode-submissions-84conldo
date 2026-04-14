class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        b = True
        li = [3,6,9]
        for num in li:
            new = []
            for i in range(num-3, num):
                for j in range(num-3, num):
                    if board[i][j] != ".":
                        new.append(board[i][j])

            if len(new) != len(set(new)):
                b = False
        
        for i in range(9):
            new = []
            for j in range(9):
                if board[i][j] != ".":
                    new.append(board[i][j])
            if len(new) != len(set(new)):
                b = False

        for i in range(9):
            new = []
            for j in range(9):
                if board[j][i] != ".":
                    new.append(board[j][i])
            if len(new) != len(set(new)):
                b = False

        return b


        