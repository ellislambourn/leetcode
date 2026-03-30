class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """ 
        tree properties:
        - It must be connected (all nodes are reachable from any other node)
        - It must have no cycles (there's exactly one path between any two nodes)
        - For n nodes, a tree must have exactly n - 1 edges
        """

        if len(edges) > (n - 1):
            return False

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()

        q = deque([(0,-1)]) # curr node, parent node
        visited.add(0)

        while q:
            node, parent = q.popleft()
            for nei in adj[node]:
                if nei == parent:
                    continue
                if nei in visited:
                    return False
                q.append((nei, node))
                visited.add(nei)

        return len(visited) == n
