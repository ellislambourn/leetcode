# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # iterative dfs with one stack
        stack = [(p,q)]
        
        while stack:
            nodes = stack.pop()
            if not any(nodes):
                continue
            if not all(nodes) or nodes[0].val != nodes[1].val:
                return False # checks if only one is None as well as chcks theyre values once established they are nodes.

            stack.append((nodes[0].left, nodes[1].left))
            stack.append((nodes[0].right, nodes[1].right))
        
        else:
            return True