# question can be found on leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/
# the solution above is elegant
# the solution below is my hack to append 0 where necessary,
# question doesn't ask a set to be returned anyways :lel:
from Typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        return range(1 - n, n, 2)

    def sumZero(self, n: int) -> List[int]:
        some = []
        if n == 1:
            some.append(0)
        elif n == 2:
            some.extend([-1, 1])
        elif n > 2:
            if n % 2 != 0:
                some.append(0)
            for num in range(1, n // 2 + 1):
                some.extend([-num, num])
        return some
