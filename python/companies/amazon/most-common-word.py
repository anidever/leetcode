import heapq


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        hashmap = {}

        paragraph = paragraph.replace(",", " ").lower().split()
        for word in paragraph:
            if not word[-1].isalnum():
                word = word[:-1]
            if word not in banned:
                if word in hashmap:
                    hashmap[word] += 1
                else:
                    hashmap[word] = 1

        return sorted(hashmap, key=hashmap.get, reverse=True)[0]


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        hashmap = {}

        paragraph = paragraph.replace(",", " ")
        for word in paragraph.lower().split():
            if not word[-1].isalnum():
                word = word[:-1]
            if word not in banned:
                if word in hashmap:
                    hashmap[word] += 1
                else:
                    hashmap[word] = 1

        heap = []

        for string, count in hashmap.items():
            heapq.heappush(heap, (-count, string))

        return heapq.heappop(heap)[1]