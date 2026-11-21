class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R, C = len(board), len(board[0])
        path = set()

        def dfs(row, col, curr):
            if curr == len(word):
                return True

            if((row < 0 or col < 0) or
                (row >= R or col >= C) or
                (board[row][col] != word[curr]) or
                ((row, col) in path)):
                return False

            path.add((row, col))
            res = (dfs(row + 1, col, curr + 1) or
                    dfs(row, col + 1, curr + 1) or
                    dfs(row - 1, col, curr + 1) or
                    dfs(row, col - 1, curr + 1))

            path.remove((row, col))
            return res

        for i in range(R):
            for j in range(C):
                if dfs(i, j, 0):
                    return True

        return False

