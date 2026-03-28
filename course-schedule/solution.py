from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = defaultdict(list)
        
        for course, pre in prerequisites:
            graph[course].append(pre)
        
        visiting = set()
        visited = set()
        
        def dfs(node):
            if node in visiting:
                return False  # cycle
            if node in visited:
                return True   # already checked
            
            visiting.add(node)
            
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            
            visiting.remove(node)
            visited.add(node)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True