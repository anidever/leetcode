from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def is_inboundaries(row, col):
            return 0 <= row < rows and 0 <= col < cols

        def dfs(row, col, threshold):
            seen.add((row, col))

            for dr, dc in directions:
                r, c = row + dr, col + dc
                if is_inboundaries(r, c) and (r, c) not in seen:
                    if heights[r][c] >= threshold:
                        return 1 + dfs(r, c, max(threshold, heights[r][c]))


        minimum, maximum = -1, -1

        while maximum > minimum + 1:
            mid = (maximum + minimum) // 2
            seen = set()
            dfs(0, 0, mid)
