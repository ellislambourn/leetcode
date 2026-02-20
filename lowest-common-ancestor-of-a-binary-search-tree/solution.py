# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # make p < q. the ancestor a is in p < a < q so brute force would be to check every node wich would be nlogn. 
        # or i just traverse to p and then to q and keep track of nodes visited to reach them.

        # traverse to p.
        pNodes = [root]
        curr = root

        while curr.val != p.val:
            if p.val > curr.val:
                curr = curr.right
            else:
                curr = curr.left
            pNodes.append(curr)
        
        # traverse to q.
        qNodes = [root]
        curr = root

        while curr.val != q.val:
            if q.val > curr.val:
                curr = curr.right
            else:
                curr = curr.left
            qNodes.append(curr)

        # compare ancestrees (lol)

        res = root
        length = min(len(pNodes), len(qNodes))
        for i in range(length):
            if pNodes[i] is qNodes[i]:
                res = pNodes[i] 
            else:
                break
        
        return res
        
    