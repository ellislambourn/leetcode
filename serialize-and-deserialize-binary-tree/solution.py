# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Codec:

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # to serialise like leetcodes pattern, bfs is needed.
        if not root:
            return ""

        res = []
        queue = deque([root])
        while queue:
            curr = queue.popleft()
            if curr == None:
                res.append("null")
            else:
                res.append(str(curr.val))
                queue.append(curr.left)
                queue.append(curr.right)
        
        while res and res[-1] == "null":
            res.pop()

        return ",".join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "":
            return None

        data = data.split(",")
        root = TreeNode(int(data[0]))
        queue = deque([root])
        index = 1

        while queue and index < len(data):
            curr = queue.popleft()

            if index < len(data) and data[index] != "null":
                curr.left = TreeNode(int(data[index]))
                queue.append(curr.left)
            index += 1

            if index < len(data) and data[index] != "null":
                curr.right = TreeNode(int(data[index]))
                queue.append(curr.right)
            index += 1

        return root