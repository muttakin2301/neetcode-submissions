class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for n in nums:
            hashmap[n] = 1 + hashmap.get(n, 0)

        sortedmap = dict(sorted(hashmap.items(), key=lambda item: item[1], reverse=True))

        return list(sortedmap.keys())[:k]