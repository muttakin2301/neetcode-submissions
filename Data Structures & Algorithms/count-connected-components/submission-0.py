class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = [[] for i in range(n)]

        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        print(adj_list)

        visited = set()

        def dfs(u):
            visited.add(u)

            for v in adj_list[u]:
                if v not in visited:
                    dfs(v)

        count = 0

        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1

        return count