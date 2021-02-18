from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = [0]
        lookup = [0] * len(T)
        for idx in range(1, len(T)):
            while stack and T[idx] > T[stack[-1]]:
                lookup[stack[-1]] = idx - stack[-1]
                stack.pop()

            stack.append(T[idx])

        return lookup
