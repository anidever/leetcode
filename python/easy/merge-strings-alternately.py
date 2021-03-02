class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        first, second = len(word1), len(word2)
        result = ""
        for one, two in zip(word1, word2):
            result += one + two

        diff = first - second
        if not diff:
            return result
        elif diff > 0:
            result += word1[-diff:]
        else:
            result += word2[diff:]

        return result
