class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.data = []

        for i in range(len(nums)):
            if i < k:
                heapq.heappush(self.data, nums[i])
            else:
                heapq.heappushpop(self.data, nums[i])

        

    def add(self, val: int) -> int:
        if len(self.data) < self.k:
            heapq.heappush(self.data, val)
        else:
            heapq.heappushpop(self.data, val)
        return self.data[0]