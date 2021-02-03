# question can be found on leetcode.com/problems/reverse-words-in-a-string-iii/


class Solution:
    def reverseWords(self, s: str) -> str:
        clean = s.split()
        xsed = [word[::-1] for word in clean]
        return " ".join(xsed)
