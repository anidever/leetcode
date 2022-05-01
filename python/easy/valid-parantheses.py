# question can be found on leetcode.com/problems/valid-parentheses/


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {"(": ")", "{": "}", "[": "]"}
        for char in s:
            if char in hashmap:
                stack.append(char)
            else:
                if stack:
                    last_char = stack.pop()
                    if hashmap[last_char] != char:
                        return False
                else:
                    return False

        return len(stack) == 0
