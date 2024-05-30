from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {"+", "-", "*", "/"}

        for token in tokens:
            if token not in ops:
                stack.append(int(token))
            elif stack:
                first = stack.pop()
                second = stack.pop()
                if token == "+":
                    res = first + second
                elif token == "-":
                    res = second - first
                elif token == "*":
                    res = first * second
                elif token == "/":
                    if first * second >= 0:
                        res = second // first
                    else:
                        res = -1 * (abs(second)//abs(first))

                stack.append(res)

        return stack[0]
