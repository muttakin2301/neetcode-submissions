# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def isInTree(r, t):
            if not r:
                return False
            if r.val == t.val:
                return True

            return isInTree(r.left, t) or isInTree(r.right, t)

        res = root
        queue = deque([root])

        while queue:
            curr = queue.popleft()

            if isInTree(curr, p) and isInTree(curr, q):
                res = curr

            if curr.left:
                queue.append(curr.left)

            if curr.right:
                queue.append(curr.right)

        return res