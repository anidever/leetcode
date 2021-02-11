# question can be found at leetcode.com/problems/most-common-word/
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.replace(",", " ")
        banned = set(banned)
        hashmap = {}
        for word in paragraph.lower().split():
            if not word[-1].isalnum():
                word = word[:-1]
            if word not in banned:
                if word in hashmap:
                    hashmap[word] += 1
                else:
                    hashmap[word] = 1

        return sorted(hashmap, key=hashmap.get, reverse=True)[0]
