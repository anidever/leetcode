# question can be found on leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/
from typing import List


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last_idx = float("-inf")
        for idx, num in enumerate(nums):
            if num:
                if k >= idx - last_idx:
                    return False
                last_idx = idx
        return True
