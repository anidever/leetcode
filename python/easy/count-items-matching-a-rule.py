# question can be found at leetcode.com/problems/count-items-matching-a-rule/
from typing import List


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        if ruleKey == "type":
            rule = 0
        elif ruleKey == "color":
            rule = 1
        elif ruleKey == "name":
            rule = 2

        def isValid(item):
            return item[rule] == ruleValue

        return len([item for item in items if isValid(item)])
