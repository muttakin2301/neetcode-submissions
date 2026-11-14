# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [(root, False, 1)]
        maxD = 0

        while stack:
            node, doesEmit, depth = stack.pop()

            if not node:
                continue

            if doesEmit:
                maxD = max(maxD, depth)
            else:
                stack.extend([(node, True, depth), (node.right, False, depth + 1), (node.left, False, depth + 1)])
        return maxD