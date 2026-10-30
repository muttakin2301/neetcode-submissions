class Solution:
    def maxArea(self, heights: List[int]) -> int:
        size = len(heights)
        result, i, j = 0, 0, size - 1

        while i < j:
            result = max(result, min(heights[i], heights[j]) * (j - i))
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return result