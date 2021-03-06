# question can be found at leetcode.com/problems/array-partition-i/
from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[:-1:2])
