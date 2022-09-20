# question can be found at leetcode.com/problems/binary-tree-level-order-traversal
from typing import Optional, List
from abstract_data_types.binary_tree import TreeNode
from abstract_data_types.binary_tree_traversals import levelOrderIterative, levelOrderRecursive


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = levelOrderIterative(root)
        result = levelOrderRecursive(root)

        return result
