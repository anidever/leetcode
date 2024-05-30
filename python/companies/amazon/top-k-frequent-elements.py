import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        counter = {}

        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1

        for key, value in counter.items():
            heapq.heappush(heap, (-value, key))

        ans = []

        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])

        return ans