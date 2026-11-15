# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        heights = {None: 0}
        stack = [(root, False)]

        while stack:
            curr, processed = stack.pop()

            if not curr:
                continue

            if processed:
                if(abs(heights[curr.left] - heights[curr.right]) > 1):
                    return False
                heights[curr] = 1 + max(heights[curr.left], heights[curr.right])
            else:
                stack.extend([(curr, True), (curr.right, False), (curr.left, False)])

        return True