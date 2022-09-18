# question can be found at leetcode.com/problems/maximum-number-of-pairs-in-array
from typing import List

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        # My suboptimal solution
        lookup = {}
        for num in nums:
            if num in lookup:
                lookup[num] += 1
            else:
                lookup[num] = 1
        
        pairs = 0
        while [item for item in lookup.values() if item >= 2]:
            for key, value in lookup.items():
                if value >= 2:
                    nums.remove(key)
                    nums.remove(key)
                    lookup[key] -= 2
                    pairs += 1
        
        return [pairs, len(nums)]

        # Elegant solution
        pairs = 0
        single = set()

        for num in nums:
            if num in single:
                # every time you see a num for the second time, pair them
                single.remove(num)
                pairs += 1
            else:
                single.add(num)
        
        return [pairs, len(single)]
