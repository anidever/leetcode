# question can be found at leetcode.com/problems/count-good-triplets/
from typing import List
from itertools import combinations


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        # Somehow brute-force is the preferred solution
        count = 0
        size = len(arr)
        for i in range(size - 2):
            for j in range(i + 1, size - 1):
                if a >= abs(arr[i] - arr[j]):
                    for k in range(j + 1, size):
                        if b >= abs(arr[j] - arr[k]) and c >= abs(arr[i] - arr[k]):
                            count += 1

        return count
        # Using combinations is somewhat inefficient, given its going to
        # create the triplets regardless of checking for a >= abs(arr[i] - arr[j])

        def isValid(triplet):
            one, two, three = triplet[0], triplet[1], triplet[2]
            return (
                a >= abs(one - two) and b >= abs(two - three) and c >= abs(one - three)
            )

        return len([triplet for triplet in (combinations(arr, 3)) if isValid(triplet)])
