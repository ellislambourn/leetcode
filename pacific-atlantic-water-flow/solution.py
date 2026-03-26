class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])

        def bfs(starts):
            visited = set(starts)
            q = deque(starts)
            
            while q:
                r, c = q.popleft()
                
                for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                    nr, nc = r + dr, c + dc
                    
                    if (
                        0 <= nr < ROWS and
                        0 <= nc < COLS and
                        (nr, nc) not in visited and
                        heights[nr][nc] >= heights[r][c]
                    ):
                        visited.add((nr, nc))
                        q.append((nr, nc))
            
            return visited
        
        pacificStarts = [(0, c) for c in range(COLS)] + [(r, 0) for r in range(ROWS)]
        
        atlanticStarts = [(ROWS-1, c) for c in range(COLS)] + [(r, COLS-1) for r in range(ROWS)]
        
        pacific = bfs(pacificStarts)
        atlantic = bfs(atlanticStarts)
        
        return list(pacific & atlantic)