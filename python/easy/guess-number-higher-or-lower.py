# question can be found at leetcode.com/problems/guess-number-higher-or-lower/
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
def guess(num: int) -> int:
    pass


class Solution:
    def guessNumber(self, n: int) -> int:
        lo, hi = 0, n

        while hi >= lo:
            mid = (hi + lo) // 2
            xes = guess(mid)
            if not xes:
                return mid
            elif xes == -1:
                hi = mid - 1
            elif xes == 1:
                lo = mid + 1
