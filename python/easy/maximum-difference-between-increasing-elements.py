# question can be found at leetcode.com/problems/maximum-difference-between-increasing-elements
from typing import List

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        # using local maximas --> reach global maxima
        first, second = 0, 1
        diff = -1
        
        while len(nums) > second:
            if nums[second] > nums[first]:
                diff = max(diff, nums[second] - nums[first])
            else:
                first = second
            
            second += 1
        
        return diff