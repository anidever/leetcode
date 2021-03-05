# question can be found at leetcode.com/problems/can-place-flowers/
from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        def isValid(idx):
            return not flowerbed[idx - 1] and not flowerbed[idx + 1]

        flowerbed = [0] + flowerbed + [0]
        count = 0
        for idx in range(1, len(flowerbed) - 1):
            flower = flowerbed[idx]
            if not flower:
                if isValid(idx):
                    flowerbed[idx] = 1
                    count += 1

        return count >= n
