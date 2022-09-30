from typing import List

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        smalls = []
        bigs = []
        pivots = []

        for num in nums:
            if pivot > num:
                smalls.append(num)
            elif num > pivot:
                bigs.append(num)
            else:
                pivots.append(num)
        
        return smalls + pivots + bigs
