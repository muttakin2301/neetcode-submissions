class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        results = []
        size = len(nums)

        for n in range(size):
            if n > 0 and nums[n] == nums[n-1]:
                continue
            
            i = n + 1
            j = size - 1

            while i < j:
                current = nums[n] + nums[i] + nums[j]

                if current == 0:
                    results.append([nums[n], nums[i], nums[j]])
                    i += 1

                    while nums[i] == nums[i - 1] and i < j:
                        i += 1

                elif current < 0:
                    i += 1
                else:
                    j -= 1

        return results