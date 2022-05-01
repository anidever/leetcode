# question can be found at leetcode.com/problems/maximum-depth-of-binary-tree
from typing import Optional
from abstract_data_types.binary_tree import TreeNode


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # for this purpose DFS & recursion will likely to perform better,
        # but could be solved with BFS & stack as well
        if not root:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return max(left_depth, right_depth) + 1
