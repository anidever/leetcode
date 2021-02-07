from typing import List


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        time, char = releaseTimes[0], keysPressed[0]
        for idx in range(len(releaseTimes) - 1):
            diff = releaseTimes[idx + 1] - releaseTimes[idx]
            if diff > time:
                time = diff
                char = keysPressed[idx + 1]
            elif diff == time and keysPressed[idx + 1] > char:
                char = keysPressed[idx + 1]

        return char
