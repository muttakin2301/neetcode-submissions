class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        start = 0
        dup = set()

        for end in range(len(s)):
            if s[end] in dup:
                maxLength = max(maxLength, end - start)
            
            while s[end] in dup:
                dup.remove(s[start])
                start += 1

            dup.add(s[end])

        return max(maxLength, len(dup))