from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # append a tuple (value, timestamp) to the hashmap
        self.hashmap[key].append((value, timestamp))

    def search_closest(self, timestamp, values):
        lo, hi = 0, len(values) - 1

        while hi >= lo:
            mid = (hi + lo) // 2
            ts, val = values[mid][1], values[mid][0]
            if timestamp == ts:
                return val
            elif timestamp > ts:
                lo = mid + 1
            else:
                hi = mid - 1

        if hi >= 0:
            return values[hi][0]
        else:
            return ""

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap:
            return ""

        values = self.hashmap[key]
        if len(values) == 1 and timestamp >= values[0][1]:
            return values[0][0]

        closest = self.search_closest(timestamp, values)
        return closest

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)