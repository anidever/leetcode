# question can be found at leetcode.com/problems/sum-of-unique-elements
from typing import List


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        hashmap = {}
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1

        result = 0
        for key in hashmap:
            if hashmap[key] == 1:
                result += key

        return result
