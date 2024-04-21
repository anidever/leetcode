# Definition for singly-linked list.
from abstract_data_types.singly_linked_list import Node

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a

        ptr = head

        while ptr.next:
            grcodiv = gcd(ptr.val, ptr.next.val)
            new_node = ListNode(val=grcodiv, next=ptr.next)
            ptr.next = new_node
            ptr = ptr.next.next

        return head