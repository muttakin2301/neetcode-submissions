class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        visited = set()

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] == "X" or (r, c) in visited:
                return

            visited.add((r, c))
            board[r][c] = "#"
            
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)
            

        for i in range(rows):
            if board[i][0] == "O" and (i, 0) not in visited:
                dfs(i, 0)
            if board[i][cols - 1] == "O" and (i, cols - 1) not in visited:
                dfs(i, cols - 1)

        for j in range(cols):
            if board[0][j] == "O" and (0, j) not in visited:
                dfs(0, j)
            if board[rows - 1][j] == "O" and (rows - 1, j) not in visited:
                dfs(rows - 1, j)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "#":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"