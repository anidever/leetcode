# leetcode.com/problems/binary-tree-inorder-traversal/
from typing import Optional, List
from abstract_data_types.binary_tree import TreeNode
from abstract_data_types.binary_tree_traversals import inOrderIterative, inOrderRecursive


class Solution:
    def inOrderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = inOrderIterative(root)
        result = inOrderRecursive(root)

        return result
