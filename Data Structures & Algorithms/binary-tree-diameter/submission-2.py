# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diam = 0
        heights = {None: 0}
        stack = [(root, False)]

        while stack:
            curr, processed = stack.pop()

            if not curr:
                continue

            if processed:
                heights[curr] = 1 + max(heights[curr.left], heights[curr.right])
                diam = max(diam, heights[curr.left] +  heights[curr.right])
            else:
                stack.extend([(curr, True), (curr.right, False), (curr.left, False)])

        return diam
        
        