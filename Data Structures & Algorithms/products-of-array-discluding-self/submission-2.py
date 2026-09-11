class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre, post, res = [0] * len(nums), [0] * len(nums), [0] * len(nums)
        default = 1

        for i in range(len(nums)):
            pre[i] = default * nums[i]
            default *= nums[i]
        
        default = 1
        for i in range(len(nums) - 1, -1, -1):
            post[i] = default * nums[i]
            default *= nums[i]

        for i in range(len(nums)):
            if i == 0:
                res[i] = post[i+1]
            elif i == len(nums) - 1:
                res[i] = pre[i - 1]
            else:
                res[i] = pre[i - 1] * post[i + 1]

        return res