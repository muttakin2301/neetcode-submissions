# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = [(root, False)]

        while stack:
            node, isEmit = stack.pop()
            if not node:
                continue

            if isEmit:
                node.left, node.right = node.right, node.left
            else:
                stack.extend([(node, True), (node.right, False), (node.left, False)])

        return root