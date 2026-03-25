class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        numOranges = 0
        q = deque()

        def getValidSpaces(r,c):
            res = []
            if not (min(r+1,c) < 0 or r+1 == ROWS or c == COLS or grid[r+1][c] != 1):
                res.append((r+1,c))
            if not (min(r-1,c) < 0 or r-1 == ROWS or c == COLS or grid[r-1][c] != 1):
                res.append((r-1,c))
            if not (min(r,c+1) < 0 or r == ROWS or c+1 == COLS or grid[r][c+1] != 1):
                res.append((r,c+1))
            if not (min(r,c-1) < 0 or r == ROWS or c-1 == COLS or grid[r][c-1] != 1):
                res.append((r,c-1))
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    numOranges += 1
                if grid[r][c] == 2:
                    q.append((r,c))
        

        time = 0
        while q and numOranges:
            for _ in range(len(q)):
                r,c = q.popleft()

                for r, c in getValidSpaces(r,c):
                    grid[r][c] = 2
                    numOranges -= 1
                    q.append((r,c))
            time +=1

        if numOranges:
            return -1
        
        return time

        
