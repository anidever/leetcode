# question can be found on leetcode.com/problems/baseball-game/
from typing import List


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        operations = {"+", "C", "D"}
        for op in ops:
            if op not in operations:
                stack.append(int(op))
            if op == "C":
                stack.pop()
            if op == "D":
                stack.append(2 * stack[-1])
            if op == "+":
                stack.append(stack[-1] + stack[-2])

        return sum(stack)
