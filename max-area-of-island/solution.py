class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0

        def dfs(rowI, colI):
            if (rowI <0 or colI< 0  or rowI >= len(grid) or colI >= len(grid[0]) or grid[rowI][colI] == 0):
                return 0 

            grid[rowI][colI] = 0
            return 1 + (dfs(rowI+1, colI) + dfs(rowI-1, colI) +dfs(rowI, colI+1) + dfs(rowI, colI-1))

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    res = max(res, dfs(r,c))

        return res