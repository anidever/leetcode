class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, head):
        self.head = Node(head)

    def depth(self):
        if not self.head:
            return self._depth(self.head, 0)

    def _depth(self, current_node, current_depth):
        if not current_node:
            return current_depth

        left_depth = self._depth(current_node.left, current_depth)
        right_depth = self._depth(current_node.right, current_depth)
        return max(left_depth, right_depth)

    def get(self, value=None):
        if self.head:
            return self._get(value, self.head)

    def _get(self, value, current_node):
        if current_node.value > value and current_node.left:
            self._get(value, current_node.left)
        elif value > current_node.value and current_node.right:
            self._get(value, current_node.right)
        else:
            return current_node

    def append(self, value):
        if not self.head:
            self.head = Node(value)
        else:
            self._append(self.head, value)

    def _append(self, value, current_node):
        if current_node.value > value:
            if current_node.left:
                self._append(value, current_node.left)
            else:
                current_node.left = Node(value)
        elif value > current_node.value:
            if current_node.right:
                self._append(value, current_node.right)
            else:
                current_node.right = Node(value)
