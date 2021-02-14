# question can be found on leetcode.com/problems/reformat-the-string/


class Solution:
    def reformat(self, s: str) -> str:
        if len(s) == 1:
            return s
        if not s.isalnum() or s.isalpha() or s.isdigit():
            return ""

        chars = ""
        digits = ""
        result = ""
        for char in s:
            if char.isalpha():
                chars += char
            elif char.isdigit():
                digits += char

        char = True if len(chars) > len(digits) else False
        for idx in range(min(len(chars), len(digits))):
            if not char:
                result += digits[idx] + chars[idx]
            else:
                result += chars[idx] + digits[idx]

        if len(chars) > len(digits):
            adder = chars[-1]
        elif len(digits) > len(chars):
            adder = digits[-1]
        else:
            adder = ""

        return result + adder
