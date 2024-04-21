class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows, cols = len(matrix), len(matrix[0])

        top, bottom = rows - 1, 0

        while top >= bottom:
            mid = (top + bottom) // 2
            row = matrix[mid]
            if row[-1] == target or row[0] == target:
                return True
            elif row[-1] > target > row[0]:
                # found the row
                break
            else:
                if target > row[-1]:
                    bottom = mid + 1
                elif row[0] > target:
                    top = mid - 1

        hi = len(row) - 1
        lo = 0

        while hi >= lo:
            mid = (hi + lo) // 2
            if row[mid] == target:
                return True
            elif row[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1

        return False

