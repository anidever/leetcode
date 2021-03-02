# question can be found at leetcode.com/problems/maximum-number-of-coins-you-can-get/
from typing import List


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        tall = -1 * int(len(piles) / 3)
        return sum(piles[1:tall:2])
