class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= (-1)

        heapq.heapify(stones)

        while stones and len(stones) >= 2:
            x = -heapq.heappop(stones)
            y = -heapq.heappop(stones)

            if x == y:
                continue

            heapq.heappush(stones, -(x - y))

        if stones:
            return -stones[0]

        return 0
