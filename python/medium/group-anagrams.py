from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        sorted_strs = sorted([sorted(string) for string in strs])
        anagrams = set("".join(tuple(row)) for row in sorted_strs)
        res = defaultdict(list)

        for string in strs:
            anagram = "".join(sorted(string))
            if anagram in anagrams:
                res[anagram].append(string)

        return [list(val) for val in res.values()]