class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        minv = float('inf')

        while left <= right:
            mid = (left + right) // 2
            print(nums[left], nums[mid], nums[right])

            if nums[mid] > nums[right]:
                left = mid + 1
                minv = min(minv, nums[right])
            elif nums[mid] < nums[left]:
                right = mid - 1
                minv = min(minv, nums[mid])
            else:
                minv = min(minv, nums[left])
                break

        return minv
