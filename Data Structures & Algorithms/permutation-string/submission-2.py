class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts1 = {}
        counts2 = {}
        windowSize = len(s1)

        for s in s1:
            counts1[s] = counts1.get(s, 0) + 1

        left = 0

        for right in range(len(s2)):
            counts2[s2[right]] = counts2.get(s2[right], 0) + 1
            if right >= windowSize - 1:
                if counts1 == counts2:
                    return True

                counts2[s2[left]] -= 1
                if counts2[s2[left]] == 0:
                    del counts2[s2[left]]
                left += 1
                
            print(left, right)
            

        return counts1 == counts2