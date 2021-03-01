# question can be found at leetcode.com/problems/keys-and-rooms/
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        keys = [key for key in rooms[0]]
        visited = {0}
        while keys:
            key = keys.pop(0)
            visited.add(key)
            for room in rooms[key]:
                if room not in visited:
                    keys.append(room)

        return len(rooms) == len(visited)
