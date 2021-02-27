# question can be found at leetcode.com/problems/find-and-replace-pattern/
from typing import List


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def mapper(word):
            lookup, string = {}, ""
            for idx, key in enumerate(word):
                if key not in lookup:
                    lookup[key] = idx
                string += str(lookup[key])

            return string

        pattern = mapper(pattern)

        def isValid(word):
            return mapper(word) == pattern

        return [word for word in words if isValid(word)]
