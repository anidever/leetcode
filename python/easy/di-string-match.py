# # question can be found on leetcode.com/problems/di-string-match/
from typing import List


class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        inc = 0
        dec = len(S)
        res = []
        for char in S:
            if char == "I":
                res.append(inc)
                inc += 1
            else:
                res.append(dec)
                dec -= 1
        if S[-1] == "I":
            res.append(res[-1] + 1)
        else:
            res.append(res[-1] - 1)
        return res
