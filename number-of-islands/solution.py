from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        # similar to dfs, ill just use a bfs function to do mark surrounding land as water.

        def bfs(rowI, colI):
            nonlocal grid
            q = deque([(rowI, colI)])
            while q:
                rowI, colI = q.popleft()
                if (rowI < 0 or 
            rowI >= len(grid) or
            colI < 0 or 
            colI >= len(grid[0]) or 
            grid[rowI][colI] == "0"):
                    continue
                grid[rowI][colI] = "0"

                q.append((rowI+1, colI))
                q.append((rowI-1, colI))
                q.append((rowI, colI+1))
                q.append((rowI, colI-1))

        for rowI in range(len(grid)):
            for colI in range(len(grid[0])):
                if grid[rowI][colI] == "1":
                    res +=1
                    bfs(rowI, colI)
        
        return res