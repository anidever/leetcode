# question can be found on leetcode.com/problems/sort-integers-by-the-number-of-1-bits/
from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort()
        ones = [(num, bin(num)[2:].count("1")) for idx, num in enumerate(arr)]
        xed = sorted(ones, key=lambda item: item[1])
        val = xed[0][1]
        if all(pair[1] == val for pair in xed):
            return arr
        else:
            return [pair[0] for pair in xed]
