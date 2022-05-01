# question can be found at leetcode.com/problems/minimum-depth-of-binary-tree
from typing import Optional
from abstract_data_types.binary_tree import TreeNode


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        stack = [root]
        result = 1
        while stack:
            size = len(stack)
            for _ in range(size):
                current = stack.pop(0)
                if not current.left and not current.right:
                    return result
                if current.left:
                    stack.append(current.left)
                if current.right:
                    stack.append(current.right)

            result += 1
