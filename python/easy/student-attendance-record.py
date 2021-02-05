# question can be found on leetcode.com/problems/student-attendance-record-i/


class Solution:
    def checkRecord(self, s: str) -> bool:
        cond1 = "LLL" not in s
        cond2 = 1 >= s.count("A")
        return cond1 and cond2
