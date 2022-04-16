from typing import Optional, List
from abstract_data_types.binary_tree import Node
from abstract_data_types.level_order_tree_traversals import preOrderRecursive, preOrderIterative


class Solution:
    def preOrderTraversalRecursive(self, root: Optional[Node]) -> List[int]:
        result = preOrderRecursive(root)
        result = preOrderIterative(root)

        return result
