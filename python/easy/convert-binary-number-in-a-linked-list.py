# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        level = 0
        level_map = {}
        level_map[level] = head.val

        while head.next:
            head = head.next
            level += 1
            level_map[level] = head.val

        total = 0
        for key, value in level_map.items():
            total += value * 2 ** (level - key - 1)

        return total
