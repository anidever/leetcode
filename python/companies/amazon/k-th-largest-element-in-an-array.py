import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            heapq.heappush(heap, -num)

        for i in range(1, k):
            heapq.heappop(heap)

        return -1 * heapq.heappop(heap)