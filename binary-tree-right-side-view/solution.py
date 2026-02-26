# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # for each layer, do a bfs by adding the right most nodes.
        res = []
        if not root:
            return res
        q = deque([root])
        levelTree = []
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)

                if node.right:
                    q.append(node.right)

                if node.left:
                    q.append(node.left) 
            
            levelTree.append(level)
        
        for level in levelTree:
            res.append(level[0])

        return res

            