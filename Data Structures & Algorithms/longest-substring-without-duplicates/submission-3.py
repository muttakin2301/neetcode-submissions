class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        start = 0
        dup = set()

        for end in range(len(s)):
            while s[end] in dup:
                dup.remove(s[start])
                start += 1

            dup.add(s[end])
            maxLength = max(maxLength, end - start + 1)

        return maxLength