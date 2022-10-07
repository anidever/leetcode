# question can be found at leetcode.com/problems/maximum-depth-of-binary-tree
from typing import Optional
from abstract_data_types.binary_tree import TreeNode

# Recursive Solution
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return max(left_depth, right_depth) + 1

# Iterative Solution
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = [root]
        result = 0

        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result += 1

        return result
