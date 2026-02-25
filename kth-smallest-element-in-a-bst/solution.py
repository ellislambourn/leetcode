# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # non optimal would do an inorder traversal then find kth index.
        res = []
        def inorder(node):
            if not node or len(res) >= k:
                return
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)
        
        inorder(root)

        return res[k-1]
