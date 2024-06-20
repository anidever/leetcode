import heapq
from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:

        result = []
        n1, n2 = len(nums1), len(nums2)
        heap = [(nums1[0] + nums2[0], 0, 0)]

        for _ in range(k):
            total, i, j = heapq.heappop(heap)
            result.append([nums1[i], nums2[j]])

            if n2 > j + 1:
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))

            if n1 > i + 1 and j == 0:
                heapq.heappush(heap, (nums1[i + 1] + nums2[j], i + 1, j))

        return result
