# question can be found on leetcode.com/problems/unique-email-addresses/
from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        adx = set()
        for email in emails:
            at_idx = email.index("@")
            sub = email[:at_idx]
            if "+" in sub:
                plus_idx = sub.index("+")
                sub = sub[:plus_idx]
            if "." in sub:
                sub = sub.replace(".", "")

            adx.add(sub + email[at_idx:])
        return len(adx)
