# question can be found at leetcode.com/problems/xor-operation-in-an-array/


class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        result = 0
        for num in range(start, n * 2 + start, 2):
            result ^= num

        return result
