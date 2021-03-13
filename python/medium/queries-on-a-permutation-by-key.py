# question can be found at leetcode.com/problems/queries-on-a-permutation-with-key/
from typing import List


class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        nums = list(range(1, m + 1))
        result = []
        for q in queries:
            idx = nums.index(q)
            result.append(idx)
            nums.insert(0, nums.pop(idx))

        return result
