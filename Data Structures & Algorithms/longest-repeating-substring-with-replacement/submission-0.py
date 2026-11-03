class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLength = 0
        count = {}
        left = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            while (right - left + 1) - max(count.values(), default=0) > k:
                count[s[left]] -= 1
                left += 1

            maxLength = max(maxLength, right - left + 1)

        return maxLength
        