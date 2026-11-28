class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = deque([])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    visited.add((i, j))
                    queue.append((i, j, 0))

        while queue:
            # print("QU - ", queue)
            r, c, dis = queue.popleft()
            grid[r][c] = min(grid[r][c], dis)

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != -1 and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc, dis + 1))

