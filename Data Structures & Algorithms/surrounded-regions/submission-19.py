class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def capture(i,j):
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != 'O':
                return
            board[i][j] = 'T' 

            capture(i+1,j)
            capture(i-1,j)
            capture(i,j+1)
            capture(i,j-1)

        for i in range(len(board)):
            if board[i][0] == 'O':
                capture(i,0)
            if board[i][-1] == 'O':
                capture(i,len(board[0]) - 1)
        
        for j in range(len(board[0])):
            if board[0][j] == 'O':
                capture(0,j)
            if board[-1][j] == 'O':
                capture(len(board) - 1,j)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'T':
                    board[i][j] = 'O'

        
        


        
        
        

            
        
        