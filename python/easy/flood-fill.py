from typing import List


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, newColor: int
    ) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        oldColor = image[sr][sc]

        def isValid(row, col):
            return (rows > row >= 0 and cols > col >= 0) and image[row][col] == oldColor

        def dfs(row, col):
            if isValid(row, col):
                image[row][col] = newColor
                [dfs(row + x, col + y) for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]]

        def bfs(row, col):
            queue = [(row, col)]
            while queue:
                row, col = queue.pop(0)
                image[row][col] = newColor
                for row, col in [
                    (row - 1, col),
                    (row + 1, col),
                    (row, col - 1),
                    (row, col + 1),
                ]:
                    if isValid(row, col):
                        queue.append((row, col))

        if oldColor != newColor:
            dfs(sr, sc)
        return image
