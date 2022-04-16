# leetcode.com/problems/binary-tree-inorder-traversal/
from typing import Optional, List
from abstract_data_types.binary_tree import Node
from abstract_data_types.level_order_tree_traversals import inOrderIterative, inOrderRecursive


class Solution:
    def inOrderTraversal(self, root: Optional[Node]) -> List[int]:
        result = inOrderIterative(root)
        result = inOrderRecursive(root)

        return result
