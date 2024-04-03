# question can be found at leetcode.com/problems/jewels-and-stones/

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewel_stones = [1 for stone in S if stone in J]
        return len(jewel_stones)
