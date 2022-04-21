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


def levelOrderRecursive(root: Optional[Node]) -> List[List[int]]:
    result = {}

    def traverse(node: Optional[Node], level: int):
        if node:
            if level not in result:
                result[level] = []

            result[level].append(node.val)
            traverse(node.left, level+1)
            traverse(node.right, level+1)

    traverse(root, 0)
    return list(result.values())


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


def levelOrderIterative(root: Optional[Node]) -> List[List[int]]:
    result = []
    if not root:
        return result

    queue = [root]
    while queue:
        size = len(queue)
        current_level = []
        for _ in size:
            current_node = queue.pop(0)
            current_level.append(current_node)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

        result.append(current_level)

    return result
