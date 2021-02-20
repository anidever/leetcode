# question can be found at leetcode.com/problems/max-increase-to-keep-city-skyline/
from typing import List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        counter = 0
        max_rows = [max(row) for row in grid]
        max_cols = [max(col) for col in zip(*grid)]
        for idx_col in range(len(grid)):
            for idx_row in range(len(grid[0])):
                counter += (
                    min(max_rows[idx_col], max_cols[idx_row]) - grid[idx_col][idx_row]
                )

        return counter
