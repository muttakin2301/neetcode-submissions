class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)

        par = [i for i in range(N + 1)]
        rank = [1] * (N + 1)

        def findParent(n):
            if par[n] != n:
                par[n] = findParent(par[n])
            return par[n]

        def union(n1, n2):
            p1, p2 = findParent(n1), findParent(n2)

            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += 1
            else:
                par[p1] = p2
                rank[p2] += 1

            return p1 == p2

        for u, v in edges:
            if union(u, v):
                return [u, v]

        