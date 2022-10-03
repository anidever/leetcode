# question can be found at leetcode.com/problems/count-nodes-equal-to-average-of-subtree
from typing import Optional
from abstract_data_types.binary_tree import TreeNode

class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.result = 0 
        
        def traverse(node) -> tuple:
            if not node:
                return (0, 0)
            
            left_sum, left_node_count = traverse(node.left)
            right_sum, right_node_count = traverse(node.right)
            
            total = left_sum + right_sum + node.val
            count = left_node_count + right_node_count + 1
            
            if total // count == node.val:
                self.result += 1
            
            return total, count


        traverse(root)
        
        return self.result