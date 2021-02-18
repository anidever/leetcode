# question can be found at leetcode.com/problems/next-greater-element-i/
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = {}
        stack = [nums2[0]]
        for idx in range(len(nums2)):
            while stack and nums2[idx] > stack[-1]:
                hashmap[stack[-1]] = nums2[idx]
                stack.pop()

            stack.append(nums2[idx])

        for num in stack:
            hashmap[num] = -1

        return [hashmap[key] for key in nums1]
