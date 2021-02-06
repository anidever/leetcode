# average-salary-excluding-the-minimum-and-maximum-salary
class Solution:
    def average(self, salary: List[int]) -> float:
        lo = 1e6
        hi = 1e3
        total = 0
        for num in salary:
            if num > hi:
                hi = num
            if lo > num:
                lo == num

            total += num

        return (total - hi - lo) / (len(salary) - 2)
