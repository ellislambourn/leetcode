# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # this sounds recursive
        # edit -  yep you got that right

        def rec(root):
            if not root:
                return float("-inf"), 0
            
            leftMax, leftGain = rec(root.left)
            rightMax, rightGain = rec(root.right)

            leftGain = max(leftGain, 0)
            rightGain = max(rightGain, 0)

            path = leftGain + root.val + rightGain

            pathMax = max(leftMax, rightMax, path)

            return pathMax, root.val + max(leftGain, rightGain)

        res, _ = rec(root)

        return res