# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        preorder = [root, left..., right...]
        inorder  = [left..., root, right...]

        First element of preorder is always the root.

        Find that root in inorder.

        Everything left of it in inorder → left subtree.

        Everything right of it in inorder → right subtree.

        Recursively repeat.

        """

        # create map for value : index in inorder
        valueToIndex = {val : i for i, val in enumerate(inorder)}

        self.preIndex = 0
        
        root = TreeNode(preorder[0])

        def rec(l, r):
            if l> r: 
                return None

            rootVal = preorder[self.preIndex]
            self.preIndex +=1
            root = TreeNode(rootVal)
            mid = valueToIndex[rootVal]
            root.left = rec(l, mid -1)
            root.right = rec(mid+1, r)
            return root

        return rec(0, len(inorder) -1)