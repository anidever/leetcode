import heapq


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        heap = []
        rows = len(matrix)
        cols = len(matrix[0])

        for row in range(rows):
            for col in range(cols):
                heapq.heappush(heap, matrix[row][col])

        if k == 1:
            return matrix[0][0]

        for _ in range(k):
            item = heapq.heappop(heap)

        return item