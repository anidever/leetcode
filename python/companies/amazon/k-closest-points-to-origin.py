import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def compute_distance(x, y):
            return math.sqrt(x ** 2 + y ** 2)

        heap = []
        for point in points:
            heapq.heappush(heap, (compute_distance(point[0], point[1]), point))

        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])

        return ans