class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])
        visited = set()
        count = 0

        def dfs(r, c):
            if r < 0 or r >= row or c < 0 or c >= col:
                return

            if grid[r][c] == "1" and (r, c) not in visited:
                visited.add((r, c))

                dfs(r, c + 1)
                dfs(r, c - 1)
                dfs(r + 1, c)
                dfs(r - 1, c)

        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1" and (i, j) not in visited:
                    dfs(i, j)
                    count += 1

        return count