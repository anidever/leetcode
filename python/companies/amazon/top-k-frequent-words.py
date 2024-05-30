import heapq


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        heap = []
        counter = {}

        for word in words:
            if word in counter:
                counter[word] += 1
            else:
                counter[word] = 1

        for key, value in counter.items():
            heapq.heappush(heap, (-value, key))

        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])

        return ans