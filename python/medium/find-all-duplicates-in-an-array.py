# question can be found at leetcode.com/problems/find-all-duplicates-in-an-array/
from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # taking advantage of question description
        # 1 ≤ a[i] ≤ n (n = size of array)
        # flip the sign of seen nums
        result = []
        for n in nums:
            ind = abs(n) - 1
            if 0 > nums[ind]:
                result.append(abs(n))
            nums[ind] *= -1

        return result
