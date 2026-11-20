class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, sub = [], []

        def dfs(start, total):
            if total > target:
                return
            if total == target:
                res.append(sub.copy())

            for i in range(start, len(nums)):
                sub.append(nums[i])
                # total += nums[i]    
                dfs(i, total + nums[i])
                # total -= nums[i]
                sub.pop()

        dfs(0, 0)

        return res
