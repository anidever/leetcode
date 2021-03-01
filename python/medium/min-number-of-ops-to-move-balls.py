# question can be found at leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/
from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ones = [idx for idx in range(len(boxes)) if int(boxes[idx])]
        return [sum([abs(one - idx) for one in ones]) for idx in range(len(boxes))]
