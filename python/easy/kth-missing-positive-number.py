# question can be found on leetcode.com/problems/kth-missing-positive-number/
from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        arr = set(arr)
        idx = 1
        missings = []
        while k > len(missings):
            if idx not in arr:
                missings.append(idx)

            idx += 1

        return idx - 1
