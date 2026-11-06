class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxp = max(piles)
        mink = maxp
        left, right = 1, maxp

        while left <= right:
            hourTaken = 0
            mid = (left + right) // 2

            for j in range(len(piles)):
                hourTaken += math.ceil(piles[j] / mid) 
            
            if hourTaken <= h:
                mink = min(mink, mid)
                right = mid - 1
            else:
                left = mid + 1
            

        return mink