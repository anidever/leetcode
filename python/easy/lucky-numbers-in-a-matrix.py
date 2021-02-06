# question can be found on leetcode.com/problems/lucky-numbers-in-a-matrix/
from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        row_mins = [min(row) for row in matrix]
        col_maxs = [max(col) for col in zip(*matrix)]
        return [num for num in row_mins if num in col_maxs]
