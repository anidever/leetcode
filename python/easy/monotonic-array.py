from typing import List


class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        # one pass
        inc = A[-1] > A[0]
        for idx in range(len(A) - 1):
            if A[idx + 1] > A[idx] and not inc:
                return False
            elif A[idx] > A[idx + 1] and inc:
                return False

        return True

        # two pass
        inc = True if all(y >= x for x, y in zip(A, A[1:])) else False
        dec = True if all(x >= y for x, y in zip(A, A[1:])) else False

        return inc or dec
