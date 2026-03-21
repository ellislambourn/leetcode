class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0

        def dfs(rowI, colI):
            nonlocal grid
            if (rowI < 0 or 
            rowI >= len(grid) or
            colI < 0 or 
            colI >= len(grid[0]) or 
            grid[rowI][colI] == "0"):
                return
            
            grid[rowI][colI] = "0"
            dfs(rowI+1, colI)
            dfs(rowI-1, colI)
            dfs(rowI, colI+1)
            dfs(rowI, colI-1)
             

        for rowI in range(len(grid)):
            for colI in range(len(grid[0])):
                if grid[rowI][colI] == "1":
                    res += 1
                    dfs(rowI, colI)
        
        return res
