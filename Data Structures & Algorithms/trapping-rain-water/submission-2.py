class Solution:
    def trap(self, height: List[int]) -> int: 
        size, totalWater = len(height), 0
        rmaxs = [0] * size
        rmax = lmax = 0
        for i in range(size - 1, -1, -1):
            rmaxs[i] = rmax
            rmax = max(height[i], rmax)

        for i in range(size):
            minh = min(lmax, rmaxs[i])
            if height[i] < minh:
                totalWater += (minh - height[i])

            lmax = max(height[i], lmax)

        return totalWater
