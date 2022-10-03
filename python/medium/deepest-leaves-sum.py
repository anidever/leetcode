from typing import Optional
from abstract_data_types.binary_tree import TreeNode

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        
        def maxDepth(node):
            if not node:
                return 0
            
            left_depth = maxDepth(node.left)
            right_depth = maxDepth(node.right)
            
            return max(left_depth, right_depth) + 1
        
        def traversal(node, level):
            if not node:
                return 0
            
            if level == self.max_depth:
                return node.val
            
            return traversal(node.left, level + 1) + traversal(node.right, level + 1)

        self.max_depth = maxDepth(root) - 1
        return traversal(root, 0)