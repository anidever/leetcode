# question can be found at leetcode.com/problems/find-common-characters/
from typing import List


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        maps = []
        for word in A:
            hashmap = {}
            for char in word:
                if char in hashmap:
                    hashmap[char] += 1
                else:
                    hashmap[char] = 1

            maps.append(hashmap)

        common_keys = set.intersection(*map(set, maps))
        common_chars = {key: 1e6 for key in common_keys}
        for lookup in maps:
            for key in common_keys:
                common_chars[key] = min(common_chars[key], lookup[key])

        # common_chars = maps[0]
        # for lookup in maps[1:]:
        #     int_keys = common_chars.keys() & lookup.keys()
        #     common_chars = {key: min(common_chars[key], lookup[key]) for key in int_keys}

        result = []
        for char in common_chars:
            adder = [char] * common_chars[char]
            result.extend(adder)

        return result
