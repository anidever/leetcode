# question can be found at leetcode.com/problems/number-of-islands/
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        num_islands = 0

        def isValid(row, col):
            return cols > col >= 0 and rows > row >= 0 and int(grid[row][col])

        def visit(row, col):
            grid[row][col] = 0

        def dfs(row, col):
            visit(row, col)
            for row, col in (
                (row + 1, col),
                (row - 1, col),
                (row, col + 1),
                (row, col - 1),
            ):
                if isValid(row, col):
                    dfs(row, col)

        def bfs(row, col):
            visit(row, col)
            queue = [(row, col)]
            while queue:
                row, col = queue.pop(0)
                for row, col in (
                    (row + 1, col),
                    (row - 1, col),
                    (row, col + 1),
                    (row, col - 1),
                ):
                    if isValid(row, col):
                        visit(row, col)
                        queue.append((row, col))

        for row in range(rows):
            for col in range(cols):
                if int(grid[row][col]):
                    num_islands += 1
                    bfs(row, col)

        return num_islands
