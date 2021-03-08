class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node()

    def length(self):
        current_node = self.head
        total = 0
        while current_node.next:
            current_node = current_node.next
            total += 1

        return total

    def __repr__(self):
        items = []
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
            items.append(current_node.value)

        return items

    def get(self, index=None, value=None):
        if index:
            if index >= self.length():
                return None
        elif not value:
            return None

        current_node, current_idx = self.head, 0
        while current_node.next:
            current_node = current_node.next
            if current_idx == index or current_node.value == value:
                return current_node.value
            else:
                current_idx += 1

    def append(self, value):
        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        new_node = Node(value)
        current_node.next = new_node

    def delete(self, index=None, value=None):
        if index:
            if index >= self.length():
                return None
        elif not value and not index:
            return None

        current_node, current_idx = self.head, 0
        while current_node.next:
            current_node = current_node.next
            if current_idx == index or current_node.value == value:
                current_node.next = None
                return None
            else:
                current_idx += 1
