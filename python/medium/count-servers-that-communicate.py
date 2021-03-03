# question can be found at leetcode.com/problems/count-servers-that-communicate/
from typing import List


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        count = 0
        col_sums = [sum(col) for col in zip(*grid)]
        for idx in range(len(grid)):
            xum = sum(grid[idx])
            if xum > 1:
                count += xum
            elif xum:
                one_idx = grid[idx].index(1)
                if col_sums[one_idx] > 1:
                    count += 1
        return count
