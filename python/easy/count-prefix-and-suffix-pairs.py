# question can be found on leetcode.com/problems/count-prefix-and-suffix-pairs-i/
from typing import List


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        size = len(words)
        count = 0

        def isPrefixAndSuffix(str1, str2) -> bool:
            length = len(str1)
            if str2[:length] == str2[-length:] == str1 or str1 == str2:
                return True
            else:
                return False

        for index in range(size - 1):
            first_str = words[index]
            for second_str in words[index + 1:]:
                if isPrefixAndSuffix(first_str, second_str):
                    count += 1

        return count

class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word):
        pass



class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
