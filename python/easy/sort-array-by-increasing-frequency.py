# question can be found on leetcode.com/problems/sort-array-by-increasing-frequency/
from typing import List


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        hashmap = {}
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1

        lookup = {}
        for key in hashmap:
            if hashmap[key] in lookup:
                lookup[hashmap[key]].append(key)
            else:
                lookup[hashmap[key]] = [key]

        result = []
        for key in sorted(lookup.keys()):
            adder = key * lookup[key]
            if len(lookup[key]) > 1:
                for innerkey in sorted(lookup[key], reverse=True):
                    adder = key * [innerkey]
                    result.extend(adder)
            else:
                result.extend(adder)

        return result
