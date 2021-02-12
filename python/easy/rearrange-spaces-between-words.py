# question can be found on leetcode.com/problems/rearrange-spaces-between-words/


class Solution:
    def reorderSpaces(self, text: str) -> str:
        spaces = text.count(" ")
        words = text.split()
        word_count = len(words)
        if word_count == 1:
            return words[0] + " " * spaces

        num, denom = divmod(spaces, word_count - 1)
        result = words[0]
        for idx in range(word_count - 1):
            result += " " * num + words[idx + 1]

        return result + " " * denom
