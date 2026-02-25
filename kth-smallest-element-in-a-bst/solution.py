# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # optimal is to do inorder traversal but just return the val once k nodes have been visited.
        res = root.val
        
        def inorder(node):
            nonlocal k, res
            if not node:
                return
            inorder(node.left)
            k -= 1
            if k == 0:
                res = node.val
                return
            inorder(node.right)
        
        inorder(root)
        return res
