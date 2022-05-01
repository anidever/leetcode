# # question can be found at leetcode.com/problems/binary-tree-postorder-traversal/
from typing import Optional, List
from abstract_data_types.binary_tree import TreeNode
from abstract_data_types.binary_tree_traversals import postOrderIterative, postOrderRecursive


class Solution:
    def postOrderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = postOrderIterative(root)
        result = postOrderRecursive(root)

        return result
