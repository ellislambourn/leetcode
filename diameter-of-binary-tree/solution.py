# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # dfs approach of giving each node its max diameter that it is involved.
        # dfs depth function:
        self.res = 0 
        def depth(root):
            global res
            if not root: return 0  
            left = depth(root.left)
            right = depth(root.right)
            
            d = 1 + max(left, right)

            self.res = max(self.res, left + right)
            return d
        
        depth(root)
        return self.res