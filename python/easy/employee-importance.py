"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""
from typing import List


class Solution:
    def getImportance(self, employees: List["Employee"], id: int) -> int:
        id_pool = [id]
        ctr = 0
        employees = {emp.id: emp for emp in employees}
        while id_pool:
            search = id_pool.pop(0)
            found = employees.get(search)
            ctr += found.importance
            id_pool += found.subordinates

        return ctr

    # def getImportance(self, employees: List["Employee"], id: int) -> int:
    #     id_pool = [id]
    #     ctr = 0
    #     while id_pool:
    #         search = [emp for emp in employees if emp.id in id_pool]
    #         id_pool = []
    #         for emp in search:
    #             ctr += emp.importance
    #             employees.remove(emp)
    #             id_pool.extend(emp.subordinates)

    #     return ctr
