# question can be found at leetcode.com/problems/rank-transform-of-an-array/
from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        yarr = sorted(set(arr))
        lookup = {num: idx + 1 for idx, num in enumerate(yarr)}
        return [lookup.get(num) for num in arr]
