# question can be found on leetcode.com/problems/smallest-range-i/
from typing import List


class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        mini = min(A) + K
        maxi = max(A) - K
        if maxi >= mini:
            return maxi - mini
        else:
            return 0
