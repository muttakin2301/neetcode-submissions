class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store = set(nums)
        maxLen = 0

        for n in nums:
            if n - 1 not in store:
                len = 1;
                while n + len in store:
                    len += 1

                maxLen = max(maxLen, len)

        return maxLen


        