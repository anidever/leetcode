from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1

        while hi >= lo:
            mid = (lo + hi) // 2
            value = nums[mid]

            if value == target:
                return mid
            elif target > value:
                lo = mid + 1
            else:
                hi = mid - 1

        return -1
