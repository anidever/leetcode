# question can be found on leetcode.com/problems/two-furthest-houses-with-different-colors
from typing import List

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        size = len(colors)
        first, second = 0, size-1
        max_distance = 0
        
        while size > first:
            if colors[first] == colors[second]:
                second -= 1 
            else:
                max_distance = max(max_distance, second-first)
                first += 1
                second = size - 1
        
        return max_distance
