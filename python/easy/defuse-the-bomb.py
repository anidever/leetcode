# question can be found on leetcode.com/problems/defuse-the-bomb/
from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        result = []
        le = len(code)
        new = code + code
        if k > 0:
            for idx in range(le):
                start = idx + 1
                end = start + k
                result.append(sum(new[start:end]))
        elif 0 > k:
            for idx in range(le):
                start = idx + le - abs(k)
                end = idx + le
                result.append(sum(new[start:end]))
        else:
            return [0] * le

        return result
