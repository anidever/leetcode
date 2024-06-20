class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:

        # Here the nuance is that we need to traverse the array twice since the array is circular
        # Also we cant use an index map since the key can repeat

        size = len(nums)
        stack = []
        result = [-1] * size

        for i in range(size * 2):
            idx = i % size
            current = nums[idx]
            while stack and current > nums[stack[-1]]:
                last = stack.pop()
                result[last] = current

            stack.append(idx)

        return result