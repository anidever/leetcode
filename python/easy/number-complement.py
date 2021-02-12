# question can be found on leetcode.com/problems/number-complement/


class Solution:
    def findComplement(self, num: int) -> int:
        binary_str = bin(num)[2:]
        complement = ""
        for bit in binary_str:
            if int(bit):
                complement += str(0)
            else:
                complement += str(1)

        return int(complement, 2)
