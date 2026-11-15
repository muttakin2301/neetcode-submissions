# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def dfs(t1, t2):
            if not t1 and not t2:
                return True

            if not t1 or not t2:
                return False
            
            if t1.val != t2.val:
                return False

            return dfs(t1.left, t2.left) and dfs(t1.right, t2.right)

        queue = deque([root])

        while queue:
            curr = queue.popleft()
            print(curr.val)
            if dfs(curr, subRoot):
                return True

            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

        return False