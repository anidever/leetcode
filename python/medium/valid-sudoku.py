# question can be found at leetcode.com/problems/valid-sudoku/
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = list(zip(*board))

        def is_unit_valid(unit):
            clean_unit = [num for num in unit if num != '.']
            return len(set(clean_unit)) == len(clean_unit)

        def is_row_valid():
            for row in board:
                if not is_unit_valid(row):
                    return False

            return True

        def is_col_valid():
            for col in columns:
                if not is_unit_valid(col):
                    return False

            return True

        def is_sub_valid():
            for i in (0, 3, 6):
                for j in (0, 3, 6):
                    square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                    if not is_unit_valid(square):
                        return False
            return True

        return is_row_valid() and is_col_valid() and is_sub_valid()
