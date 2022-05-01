# question can be found at leetcode.com/problems/binary-tree-preorder-traversal/
from typing import Optional, List
from abstract_data_types.binary_tree import TreeNode
from abstract_data_types.binary_tree_traversals import preOrderRecursive, preOrderIterative


class Solution:
    def preOrderTraversalRecursive(self, root: Optional[TreeNode]) -> List[int]:
        result = preOrderRecursive(root)
        result = preOrderIterative(root)

        return result
