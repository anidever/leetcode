from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        size = len(temperatures)
        result = [0] * size
        stack = []

        for idx in range(size):
            current = temperatures[idx]
            while stack and current > stack[-1][0]:
                _, last_idx = stack.pop()
                result[last_idx] = idx - last_idx

            stack.append((current, idx))

        return result
