# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # bfs twice
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        queue1 = deque([p])
        queue2 = deque([q])
        
        while queue1 or queue2:
            if not (queue1 and queue2):
                return False # test if there are more nodes in one tree
            node1, node2 = queue1.popleft(), queue2.popleft()
            if not (node1.val == node2.val):
                return False
            if bool(node1.right) != bool(node2.right):
                return False
            if bool(node1.left) != bool(node2.left):
                return False
            if node1.left:
                queue1.append(node1.left)
            if node2.left:
                queue2.append(node2.left)
            if node1.right:
                queue1.append(node1.right)
            if node2.right:
                queue2.append(node2.right)
        else:
            return True
            
