

from typing import Optional, List
from abstract_data_types.binary_tree import Node
from abstract_data_types.binary_tree_traversals import levelOrderIterative, levelOrderRecursive


class Solution:
    def levelOrder(self, root: Optional[Node]) -> List[List[int]]:
        result = levelOrderIterative(root)
        result = levelOrderRecursive(root)

        return result
