from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        # 2 pass solution
        length = len(arr) - 1
        diff = min([abs(arr[idx + 1] - arr[idx]) for idx in range(length)])
        return [
            [arr[idx], arr[idx + 1]]
            for idx in range(length)
            if abs(arr[idx + 1] - arr[idx]) == diff
        ]

        # 1 pass solution
        mini = abs(arr[1] - arr[0])
        lookup = {mini: []}
        for idx in range(len(arr) - 1):
            diff = abs(arr[idx + 1] - arr[idx])
            if mini > diff:
                lookup[diff] = [[arr[idx], arr[idx + 1]]]
            elif mini == diff:
                lookup[mini].append([arr[idx], arr[idx + 1]])
            mini = min(mini, diff)

        return lookup[mini]
