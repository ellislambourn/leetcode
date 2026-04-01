class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # dfs find a cycle first then store the nodes in that cycle
        n = len(edges)
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        cycle = set()
        cycleStart = -1
        visited = [False] * (n+1)
        def dfs(node, parent):
            nonlocal cycleStart
            if visited[node]:
                cycleStart = node
                return True

            visited[node] = True
                
            for nei in adj[node]:
                if nei == parent:
                    continue
                if dfs(nei, node):
                    if cycleStart != -1:
                        cycle.add(node)
                    if node == cycleStart:
                        cycleStart = -1
                    return True
            return False

        dfs(1, -1)

        for node1, node2 in reversed(edges):
            if node1 in cycle and node2 in cycle:
                return [node1, node2]
        
        return []

        