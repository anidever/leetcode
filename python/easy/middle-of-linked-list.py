# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        index = 0
        node_index_map = {index: head}

        while head.next:
            index += 1
            node_index_map[index] = head.next
            head = head.next

        mid = (index + 1) // 2

        return node_index_map[mid]

