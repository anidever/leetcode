from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])
        rottens = []
        fresh = 0
        time = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    rottens.append((row, col))
                elif grid[row][col] == 1:
                    fresh += 1

        total_oranges = len(rottens) + fresh
        if total_oranges == 0 or fresh == 0:
            return 0

        def is_valid(i, j):
            return rows > i >= 0 and cols > j >= 0 and grid[i][j] == 1

        while rottens:
            level_size = len(rottens)
            for level in range(level_size):
                rotten_orange = rottens.pop(0)
                row, col = rotten_orange[0], rotten_orange[1]
                for row, col in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
                    if is_valid(row, col):
                        grid[row][col] = 2
                        fresh -= 1
                        rottens.append((row, col))

            time += 1

        return -1 if fresh > 0 else time - 1
