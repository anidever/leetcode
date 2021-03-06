# question can be found at https://leetcode.com/problems/top-k-frequent-elements/
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lookup = {}
        for num in nums:
            if num in lookup:
                lookup[num] += 1
            else:
                lookup[num] = 1

        result = []
        for i in range(k):
            maks = max(lookup, key=lookup.get)
            result.append(maks)
            lookup.pop(maks)

        return result

        # I am trying not to use given methods, but ..
        from collections import Counter

        a = Counter(nums)
        return [i[0] for i in a.most_common(k)]
