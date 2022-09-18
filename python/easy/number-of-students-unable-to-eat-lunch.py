# question can be found at leetcode.com/problems/number-of-students-unable-to-eat-lunch/
from typing import List

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        while students and sandwiches and sandwiches[0] in students:
            student = students.pop(0)
            if student == sandwiches[0]:
                sandwiches.pop(0)
            else:
                students.append(student)
        
        return len(students)
