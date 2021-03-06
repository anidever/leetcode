# question can be found at leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/
from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        hashmap = {}
        for idx, size in enumerate(groupSizes):
            if size in hashmap:
                hashmap[size].append(idx)
            else:
                hashmap[size] = [idx]

        result = []
        for key in hashmap:
            length = len(hashmap[key])
            if length > key:
                for i in range(0, length, key):
                    result.append(hashmap[key][i : i + key])
            else:
                result.append(hashmap[key])

        return result
        # return [
        #     hashmap[i][j : j + i] for i in hashmap for j in range(0, len(hashmap[i]), i)
        # ]
        # I commented out the above line, I think it's more elegant but hard to read
