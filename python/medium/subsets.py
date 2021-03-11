# question can be found at leetcode.com/problems/subsets/
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for sub in nums:
            result.extend([s + [sub] for s in result])

        return result
