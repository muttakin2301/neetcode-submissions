class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res, sub = [], []

        def dfs(start, total):
            if total == target:
                res.append(sub.copy())
            if total > target:
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                sub.append(candidates[i])
                dfs(i + 1, total + candidates[i])
                sub.pop()

        dfs(0, 0)

        return res