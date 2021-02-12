from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        # my solution
        subs = set()
        for idx in range(len(words)):
            for word in words:
                if words[idx] in word and not words[idx] == word:
                    subs.add(words[idx])
                    break

        return subs

        # an alternative I liked
        subs = []
        for idx in range(len(words)):
            sentence = words[idx + 1 :] + words[:idx]
            if words[idx] in " ".join(sentence):
                subs.append(words[idx])

        return subs
