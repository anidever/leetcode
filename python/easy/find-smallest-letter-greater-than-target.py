# question can be found at leetcode.com/problems/find-smallest-letter-greater-than-target/
from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        letters = sorted(set(letters))
        for letter in letters:
            if letter > target:
                return letter

        return letters[0]

        # well, binary search is faster ya know ..
        letters = sorted(set(letters))
        left, right = 0, len(letters) - 1

        while right >= left:
            mid = left + (right - left) // 2
            if target >= letters[mid]:
                left = mid + 1
            else:
                right = mid - 1

        return letters[left]
