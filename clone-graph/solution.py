"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        mapp = {}
        
        def copy(node): 
            if node in mapp:
                return mapp[node]
            
            newNode = Node(node.val)
            mapp[node] = newNode
            for neighbor in node.neighbors:
                newNode.neighbors.append(copy(neighbor))

            return newNode

        return copy(node)