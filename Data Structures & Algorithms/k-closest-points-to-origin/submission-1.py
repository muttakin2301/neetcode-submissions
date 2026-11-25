class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        store = []

        for i in range(len(points)):
            x, y = points[i]
            dis = pow(x, 2) + pow(y, 2)
            
            if len(store) < k:
                heapq.heappush(store, (-dis, (x, y)))
            else:
                heapq.heappushpop(store, (-dis, (x, y)))

        results = []
        for i in range(k):
            dist, cord = heapq.heappop(store)
            results.append(cord)

        return results
