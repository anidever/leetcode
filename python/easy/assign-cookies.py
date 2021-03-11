# question can be found at leetcode.com/problems/assign-cookies/
from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # My terrible solution
        count = 0
        s.sort(), g.sort()
        while s:
            first = s.pop(0)
            if first in g:
                count += 1
                g.remove(first)
            else:
                for pick in g:
                    if first > pick:
                        count += 1
                        g.remove(pick)
                        break

        return count

        # Better solution
        s.sort(), g.sort()
        greed, cookies = 0, 0
        while len(g) > greed and len(s) > cookies:
            if s[cookies] >= g[greed]:
                greed += 1

            cookies += 1

        return greed
