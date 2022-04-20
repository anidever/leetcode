# Level Order Traversals can be executed by depth-first search:
# Preorder root-left-right
# Inorder left-root-right
# Postorder left-right-root
from typing import Optional, List
from abstract_data_types.binary_tree import Node


# Recursive solutions
def inOrderRecursive(root: Optional[Node]) -> List[int]:
    result = []

    def traverse(node):
        if not node:
            return

        traverse(node.left)
        result.append(node.val)
        traverse(node.right)

    traverse(root)

    return result


def postOrderRecursive(root: Optional[Node]) -> List[int]:
    result = []

    def traverse(node):
        if not node:
            return

        traverse(node.right)
        result.append(node.val)
        traverse(node.left)

    traverse(root)

    return result


def preOrderRecursive(root: Optional[Node]) -> List[int]:
    result = []

    def traverse(node):
        if not node:
            return

        result.append(node.val)
        traverse(node.left)
        traverse(node.right)

    traverse(root)

    return result


# Iterative solutions
def inOrderIterative(root: Optional[Node]) -> List[int]:
    result = []
    stack = []
    current = root

    while current or stack:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        result.append(current.value)
        current = current.right

    return result


def postOrderIterative(root: Optional[Node]) -> List[int]:
    result = []
    stack = [root]
    current = root

    while stack:
        current = stack.pop()
        if current:
            result.insert(0, current.value)
            stack.append(current.left)
            stack.append(current.right)

    return result


def preOrderIterative(root: Optional[Node]) -> List[int]:
    result = []
    stack = []
    current = root

    while stack or current:
        while current:
            stack.append(current)
            result.append(current.value)
            current = current.left

        current = stack.pop()
        current = current.right

    return result
