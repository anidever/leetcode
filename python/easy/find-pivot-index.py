# question can be found on leetcode.com/problems/find-pivot-index/
from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        leftSum = 0
        for idx, num in enumerate(nums):
            if total - num == 2 * (leftSum):
                return idx
            else:
                leftSum += num

        return -1
