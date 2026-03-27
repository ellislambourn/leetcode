class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = set()
        ROWS = len(board)
        COLS = len(board[0])

        def dfs(r,c):
            board[r][c] = "T"
            if r+1 != ROWS and board[r+1][c] == "O":
                dfs(r+1, c)
            if r != 0 and board[r-1][c] == "O":
                dfs(r-1, c)
            if c+1 != COLS and board[r][c+1] == "O":
                dfs(r, c+1)    
            if c != 0 and board[r][c-1] == "O":
                dfs(r, c-1)

        for r in range(ROWS):
            if board[r][0] == "O":
                dfs(r,0)
            if board[r][COLS-1] == "O":
                dfs(r,COLS-1)
            
        for c in range(COLS):
            if board[0][c] == "O":
                dfs(0,c)
            if board[ROWS-1][c] == "O":
                dfs(ROWS-1, c)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"


