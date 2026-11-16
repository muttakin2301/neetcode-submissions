# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(curr, maxn):
            if not curr:
                return 0

            if curr.val >= maxn:
                return 1 + dfs(curr.left, max(maxn, curr.val)) + dfs(curr.right, max(maxn, curr.val))

            return dfs(curr.left, max(maxn, curr.val)) + dfs(curr.right, max(maxn, curr.val))

        return dfs(root, root.val)