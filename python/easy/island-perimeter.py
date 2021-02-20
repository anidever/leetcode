from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        seen = set()
        rows = len(grid)
        cols = len(grid[0])
        perimeter = 0

        def dfs(row, col):
            if (row, col) in seen:
                return 0

            if row >= rows or col >= cols or 0 > col or 0 > row or not grid[row][col]:
                return 1

            seen.add((row, col))
            if grid[row][col]:
                return (
                    dfs(row - 1, col)
                    + dfs(row + 1, col)
                    + dfs(row, col - 1)
                    + dfs(row, col + 1)
                )

        for row in range(rows):
            for col in range(cols):
                if grid[row][col]:
                    perimeter += dfs(row, col)

        return perimeter

        ## Alternative I liked
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]:
                    perimeter += 4
                    if row > 0 and grid[row - 1][col]:
                        perimeter -= 2
                    if col > 0 and grid[row][col - 1]:
                        perimeter -= 2
