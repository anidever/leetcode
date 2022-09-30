from typing import Optional
from abstract_data_types.binary_tree import TreeNode

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.lefts = []
        
        def traverse(node):
            queue = [node]
            
            while queue:
                current_node = queue.pop()
                if current_node.left:
                    queue.append(current_node.left)
                    left_node = current_node.left
                    if not left_node.left and not left_node.right:
                        self.lefts.append(left_node)
                if current_node.right:
                    queue.append(current_node.right)                
            
        
        traverse(root)
        return sum([node.val for node in self.lefts])
