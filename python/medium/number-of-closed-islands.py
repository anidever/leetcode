class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def is_valid(row, col):
            return cols - 1 > col >= 0 and rows - 1 > row >= 0 and grid[row][col] == 0

        def dfs(row, col):
            stack = [(row, col)]

            while stack:
                row, col = stack.pop()
                grid[row][col] = 1
                for row, col in (
                    (row + 1, col),
                    (row - 1, col),
                    (row, col + 1),
                    (row, col - 1),
                ):
                    if is_valid(row, col):
                        stack.append((row, col))

        # Mark all boundary-connected components
        # First and last rows
        for c in range(cols):
            if grid[0][c] == 0:
                dfs(0, c)
            if grid[rows - 1][c] == 0:
                dfs(rows - 1, c)

        # First and last columns
        for r in range(rows):
            if grid[r][0] == 0:
                dfs(r, 0)
            if grid[r][cols - 1] == 0:
                dfs(r, cols - 1)

        num_islands = 0
        for row in range(1, rows - 1):
            for col in range(1, cols - 1):
                if grid[row][col] == 0:
                    dfs(row, col)
                    num_islands += 1

        return num_islands
