import random


class RandomizedSet:
    def __init__(self):
        self.keys = []
        self.index_map = {}
        self.index = 0

    def insert(self, val: int) -> bool:
        if val not in self.index_map:
            self.keys.append(val)
            self.index_map[val] = self.index
            self.index += 1
            return True

        return False

    def remove(self, val: int) -> bool:
        if val in self.index_map:
            last_item = self.keys[-1]
            idx = self.index_map[val]
            self.keys[idx] = last_item
            self.index_map[last_item] = idx
            self.index -= 1
            self.keys.pop()
            del self.index_map[val]
            return True

        return False

    def getRandom(self) -> int:
        return random.choice(self.keys)
