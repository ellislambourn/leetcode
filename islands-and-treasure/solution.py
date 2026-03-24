class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        inf = 2**31 - 1 
        visited = set()
        queue = deque()
        
        def addCell(r, c):
            if (min(r, c) < 0 or r == len(grid) or c == len(grid[0]) or
                (r, c) in visited or grid[r][c] == -1
            ):
                return
            visited.add((r, c))
            queue.append((r, c))


        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0: # if treasure chest
                   queue.append((r,c))
                   visited.add((r,c))
    
        curr = 0
        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()
                grid[r][c] = curr
                addCell(r+1,c)
                addCell(r-1,c)
                addCell(r,c+1)
                addCell(r,c-1)
            curr += 1
