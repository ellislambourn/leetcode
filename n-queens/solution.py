class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = ["." * n] * n

        def rec(row):
            if row >= n:
                res.append(board.copy())
                return
            
            for col in range(n):
                if check():
                    board[row][col] = "." * + "Q" + "." *
                    rec(row+1)
                    board[row][col] = "." * n


    def check(self, coords):
