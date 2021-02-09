# question can be found on leetcode.com/problems/maximum-number-of-balloons/


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hashmap = {"b": 0, "a": 0, "l": 0, "o": 0, "n": 0}
        for char in text:
            if char in hashmap:
                hashmap[char] += 1

        min_ban = min(hashmap["b"], hashmap["a"], hashmap["n"])
        min_lo = min(hashmap["l"], hashmap["o"])
        return min(min_ban, min_lo // 2)
