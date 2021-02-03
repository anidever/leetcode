# question can be found on leetcode.com/problems/find-the-highest-altitude/

from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest, altitude = 0, 0
        for step in gain:
            altitude += step
            highest = max(altitude, highest)

        return highest
