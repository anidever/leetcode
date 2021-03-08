from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort(reverse=True)
        while len(stones) > 1:
            first, second = stones.pop(0), stones.pop(0)
            stones.append(abs(first - second))
            stones.sort(reverse=True)

        return stones[0]
