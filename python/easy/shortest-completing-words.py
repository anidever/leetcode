# question can be found at leetcode.com/problems/shortest-completing-word/
from typing import List


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        plateMap = self.mapper(licensePlate)
        potentials = [word for word in words if self.comp(self.mapper(word), plateMap)]
        return sorted(potentials, key=len)[0]

    def comp(self, map1, map2):
        for key1 in map2:
            if key1 in map1 and map1[key1] >= map2[key1]:
                continue
            else:
                return False
        return True

    def mapper(self, word):
        clean = "".join(filter(str.isalpha, word)).upper()
        lookup = {}
        for char in clean:
            if char in lookup:
                lookup[char] += 1
            else:
                lookup[char] = 1

        return lookup
