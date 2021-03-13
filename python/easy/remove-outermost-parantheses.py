# question can be found at leetcode.com/problems/remove-outermost-parentheses/


class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        count = 0
        result = ""
        for char in S:
            if char == "(":
                count += 1
            if count > 1:
                result += char
            if char == ")":
                count -= 1

        return result

        # A solution with unneccessary extra space
        # by storing primitive start-end indices
        indices = []
        last, count = 0, 0
        for idx in range(len(S)):
            if S[idx] == "(":
                count += 1
            else:
                count -= 1

            if not count:
                indices.append([last, idx])
                last = idx + 1

        result = ""
        for start, end in indices:
            result += S[start + 1 : end]

        return result
