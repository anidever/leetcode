class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # My half ass solution
        def isCovered(first, second):
            start1, end1 = first[0], first[1]
            start2, end2 = second[0], second[1]
            return start2 >= start1 and end1 >= end2 and first != second

        covered = set(
            (
                tuple(item2)
                for item1 in intervals
                for item2 in intervals
                if isCovered(item1, item2)
            )
        )

        return len(intervals) - len(covered)

        # Preferred solution
        intervals.sort(key=lambda x: (x[0], -x[1]))
        counter, comp = 0, -1
        for start, end in intervals:
            if end > comp:
                counter += 1
                comp = end

        return counter
