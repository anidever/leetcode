from typing import Optional
from abstract_data_types.binary_tree import TreeNode

class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:

        def traverse(node):
            if not node:
                return
            
            left = traverse(node.left)
            right = traverse(node.right)
            
            if node.val == 2:
                return left or right
            elif node.val == 3:
                return left and right
            else:
                return node.val
        
        return traverse(root)
