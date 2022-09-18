# question can be found on leetcode.com/problems/time-needed-to-buy-tickets/
from typing import List

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        counter = 0
        buyer = tickets[k]
        
        for ticket in tickets[:k+1]:
            counter += min(ticket, buyer)
        
        for ticket in tickets[k+1:]:
            counter += min(ticket, buyer-1)
        
        return counter
