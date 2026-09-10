class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        countAll = defaultdict(list)

        for s in strs:
            countS = [0] * 26

            for c in s:
                countS[ord(c) - ord('a')] += 1

            countAll[tuple(countS)].append(s)

        return list(countAll.values())