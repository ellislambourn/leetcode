class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        self.board = ["." * n for _ in range(n)]

        def rec(row):

            if row >= n:
                res.append(self.board.copy())
                return
            
            for col in self.check(row, n):
                self.board[row] = "." * col + "Q" + "." * (n-col-1)
                rec(row+1)
                self.board[row] = "." * n
            
        rec(0)

        return res

    def check(self, row, n) -> list[int]:
        if row == 0:
            return list(range(n))
        banned = set()
        for rIndex in range(row):
            queenI = self.board[rIndex].index("Q")
            banned.add(queenI)
            left = -(row - rIndex)
            right = -left
            if queenI + left >=0:
                banned.add(queenI+left)
            if queenI + right < n:
                banned.add(queenI + right)
            
        
        return list(set(range(n)) - banned)
