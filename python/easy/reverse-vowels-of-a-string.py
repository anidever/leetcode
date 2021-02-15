# question can be found at leetcode.com/problems/reverse-vowels-of-a-string/


class Solution:
    def reverseVowels(self, s: str) -> str:
        wovels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        indices = [char for char in s if char in wovels][::-1]
        result = ""
        ptr = 0
        for idx in range(len(s)):
            if s[idx] in wovels:
                result += indices[ptr]
                ptr += 1
            else:
                result += s[idx]

        return result
