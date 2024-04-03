# question can be found at leetcode.com/problems/minimum-amount-of-time-to-collect-garbage
from typing import List

class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        # My brute-force solution
        counter = 0
        lookup = {"G": [], "P": [], "M": []}
        
        for idx, trash in enumerate(garbage):
            for garbage_type in lookup:
                if garbage_type in trash:
                    lookup[garbage_type].append((idx))

        for garbage_type in lookup:
            if lookup[garbage_type]:
                idx = 0
                for trash in lookup[garbage_type]:
                    counter += garbage[trash].count(garbage_type) # collection time
                    counter += sum(travel[idx:trash]) # travel time 
                    idx = trash