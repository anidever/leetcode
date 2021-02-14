# question can be found on leetcode.com/problems/path-crossing/


class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x, y = 0, 0
        trip = {(x, y)}
        for step in path:
            if step == "N":
                y += 1
            elif step == "S":
                y -= 1
            elif step == "E":
                x += 1
            elif step == "W":
                x -= 1

            new = (x, y)
            if new in trip:
                return True
            else:
                trip.add(new)

        return False
