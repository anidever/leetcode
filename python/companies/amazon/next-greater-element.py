from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        hashmap = {num: idx for idx, num in enumerate(nums1)}
        stack = []
        ans = [-1] * len(nums1)

        for idx in range(len(nums2)):
            current = nums2[idx]
            while stack and current > stack[-1]:
                num = stack.pop()
                if num in hashmap:
                    ans[hashmap[num]] = current

            stack.append(current)

        return ans


