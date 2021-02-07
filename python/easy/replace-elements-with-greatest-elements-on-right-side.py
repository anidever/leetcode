# question can be found on leetcode.com/problems/

from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # my horrible solution
        arr[:] = [max(arr[idx + 1 :]) for idx, num in enumerate(arr[:-1])]

        arr.append(-1)

        return arr

        # the efficient way
        # arr = [17,18,5,4,6,1]
        rightMax = -1
        for idx in range(len(arr) - 1, -1, -1):
            newMax = max(rightMax, arr[idx])
            arr[idx] = rightMax
            rightMax = newMax

        return arr
