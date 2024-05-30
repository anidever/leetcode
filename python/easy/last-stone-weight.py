import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort(reverse=True)
        while len(stones) > 1:
            first, second = stones.pop(0), stones.pop(0)
            stones.append(abs(first - second))
            stones.sort(reverse=True)

        return stones[0]


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        heap = []

        for stone in stones:
            heapq.heappush(heap, -stone)

        while len(heap) >= 2:
            first = heapq.heappop(heap)
            second = heapq.heappop(heap)
            diff = abs(first - second)
            heapq.heappush(heap, -diff)

        return -1 * heap[0]