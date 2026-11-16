# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxPath = float('-inf')

        def dfs(curr):
            if not curr:
                return 0

            ml = max(dfs(curr.left), 0)
            mr = max(dfs(curr.right), 0)

            self.maxPath = max(self.maxPath, curr.val + ml + mr)

            return curr.val + max(ml, mr)

        dfs(root)

        return self.maxPath
            