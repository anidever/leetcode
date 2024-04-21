# question can be found at leetcode.com/problems/design-hit-counter/
from collections import deque


class HitCounter:
    def __init__(self):
        self.hits = [0] * 300
        self.timestamps = []

    def hit(self, timestamp: int) -> None:
        index = timestamp % 300
        self.hits[index] += 1
        self.timestamps.append(timestamp)

    def getHits(self, timestamp: int):
        total_hits = 0

        for i in range(300):
            if 300 > timestamp - self.timestamps[-1]:
                total_hits += self.hits[i]

        return total_hits


class HitCounter:
    def __init__(self):
        self.queue = []

    def hit(self, timestamp):
        self.queue.append(timestamp)

    def getHits(self, timestamp):
        while self.queue and timestamp - self.queue[0] >= 300:
            self.queue.pop(-1)

        return len(self.queue)


class HitCounter:
    def __init__(self):
        # Initialize a deque to store hit timestamps
        self.queue = deque()
        # Initialize an array to store hit counts for each timestamp within the last 300 seconds
        self.hits_in_window = [0] * 300

    def hit(self, timestamp):
        # Add the current timestamp to the queue
        self.queue.append(timestamp)
        # Increment the hit count for the current timestamp in the array
        self.hits_in_window[timestamp % 300] += 1

    def getHits(self, timestamp):
        # Remove timestamps that are older than 300 seconds from the queue
        while self.queue and timestamp - self.queue[0] >= 300:
            self.hits_in_window[self.queue.popleft() % 300] -= 1

        # Return the sum of hit counts for the last 300 seconds
        return sum(self.hits_in_window)