class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        rows, cols = len(grid), len(grid[0])

        def isValid(row, col):
            return cols > col >= 0 and rows > row >= 0 and grid[row][col]

        def visit(row, col):
            grid[row][col] = 0

        def dfs(row, col):
            area = 1
            visit(row, col)
            for row, col in (
                (row - 1, col),
                (row + 1, col),
                (row, col - 1),
                (row, col + 1),
            ):
                if isValid(row, col):
                    area += dfs(row, col)

            return area

        def bfs(row, col):
            area = 1
            visit(row, col)
            queue = [(row, col)]
            while queue:
                row, col = queue.pop(0)
                for row, col in (
                    (row - 1, col),
                    (row + 1, col),
                    (row, col - 1),
                    (row, col + 1),
                ):
                    if isValid(row, col):
                        area += 1
                        visit(row, col)
                        queue.append((row, col))
            return area

        for row in range(rows):
            for col in range(cols):
                if grid[row][col]:
                    max_area = max(max_area, dfs(row, col))

        return max_area
