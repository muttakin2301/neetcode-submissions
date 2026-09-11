class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        default = 1 

        for i in range(1, len(nums)):
            res[i] = default * nums[i - 1]
            default *= nums[i - 1]
        
        default = nums[len(nums) - 1]
        for i in range(len(nums) - 2, -1, -1):
            res[i] *= default
            default *= nums[i]

        return res