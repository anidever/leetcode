class Node:
    def __init__(self):
        self.children = {}
        self.isWord = False


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = Node()

            current = current.children[char]

        current.isWord = True

    def search(self, word: str) -> bool:
        """
        Searches for a word in the trie.

        Args:
          word: The word to search for.

        Returns:
          The value associated with the word if found, otherwise False
        """
        current = self.root
        for char in word:
            if char not in current.children:
                return False

            current = current.children[char]

        return current.isWord

    def startsWith(self, prefix: str) -> bool:
        """
        Checks if a given prefix exists in the trie.

        Args:
          prefix: The prefix to search for.

        Returns:
          True if the prefix exists, otherwise False.
        """
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False

            current = current.children[char]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)