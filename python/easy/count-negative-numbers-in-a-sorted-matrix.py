# question can be found on leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/
from Typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        num = 0
        for array in grid:
            for item in array:
                if item < 0:
                    num += 1
        return num

        # List comprehension
        for array in grid:
            num += len([item for item in array if item < 0])
        return num
