from typing import List

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        size = len(nums)
        pos, neg = 0, 0

        def pos_index(array):
            lo = 0
            hi = len(array) - 1

            while hi >= lo:
                mid = (hi + lo) // 2

                if array[mid] > 0:
                    hi = mid - 1
                else:
                    lo = mid + 1

            return lo

        def neg_index(array):
            lo = 0
            hi = len(array) - 1

            while hi >= lo:
                mid = (hi + lo) // 2

                if 0 > array[mid]:
                    lo = mid + 1
                else:
                    hi = mid - 1

            return hi

        if nums[0] > 0 or nums[-1] < 0:
            return size
        else:
            pos = pos_index(nums)
            neg = neg_index(nums)

        return max(size-pos, neg+1)

