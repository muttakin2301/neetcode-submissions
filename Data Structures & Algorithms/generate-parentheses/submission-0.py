class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, sub = [], ""

        def dfs(sub, opn, cls):
            print("DFS", sub, opn, cls)
            if opn == n and cls == n:
                res.append(sub)
                return

            if cls < opn:
                sub += ")"
                dfs(sub, opn, cls + 1)
                sub = sub[:-1]
            if opn < n:
                sub += "("
                dfs(sub, opn + 1, cls)
                sub = sub[:-1]
                

        dfs(sub, 0, 0)
        return res