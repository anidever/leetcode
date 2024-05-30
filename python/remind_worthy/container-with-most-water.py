# question can be found on leetcode.com/problems/container-with-most-water/
from Typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        result, start, end = 0, 0, len(height) - 1
        while end > start:
            result = max(result, (end - start) * min(height[start], height[end]))
            if height[start] > height[end]:
                end -= 1
            else:
                start += 1
        return result
