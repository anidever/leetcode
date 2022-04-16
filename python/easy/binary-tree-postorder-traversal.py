# leetcode.com/problems/binary-tree-inorder-traversal/
from typing import Optional, List
from abstract_data_types.binary_tree import Node
from abstract_data_types.level_order_tree_traversals import postOrderIterative, postOrderRecursive


class Solution:
    def postOrderTraversal(self, root: Optional[Node]) -> List[int]:
        result = postOrderIterative(root)
        result = postOrderRecursive(root)

        return result
