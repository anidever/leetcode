# question can be found at leetcode.com/problems/number-of-segments-in-a-string/


class Solution:
    def countSegments(self, s: str) -> int:
        word = 0
        count = 1

        for char in s:
            if char != " " and count:
                word += 1
                count = 0
            if char == " ":
                count = 1

        return word
        # return len(s.split())
