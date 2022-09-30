from typing import List

class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        self.bucket = capacity
        self.steps, idx = 0, 0
        
        def water(plant):
            self.bucket -= plant
            self.steps += 1
        
        def refill(index):
            self.bucket = capacity
            self.steps += index * 2

        while len(plants) > idx:
            current_plant = plants[idx]
            if self.bucket >= current_plant:
                water(current_plant)
                idx += 1
            else:
                refill(idx)
        
        return self.steps
