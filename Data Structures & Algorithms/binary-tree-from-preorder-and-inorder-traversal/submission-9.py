# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.preorder = preorder
        self.inorder = inorder
        self.index = {}

        for i in range(len(inorder)):
            self.index[self.inorder[i]] = i

        def dfs(pl, pr, il, ir):
            if pl > pr or il > ir:
                return None

            curr = TreeNode(self.preorder[pl])
            mid = self.index[self.preorder[pl]]
            curr.left = dfs(pl+1, pl+(mid-il), il, mid - 1)
            curr.right = dfs(pl+(mid-il) + 1, pr, mid + 1, ir)

            return curr

        return dfs(0, len(preorder) - 1, 0, len(inorder) - 1)
