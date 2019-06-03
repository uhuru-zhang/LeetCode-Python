class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        current_dict = self.trie
        for c in word:
            if c not in current_dict:
                current_dict[c] = {}
            current_dict = current_dict[c]
        current_dict["END"] = "END"

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        current_dict = self.trie
        for c in word:
            if c not in current_dict:
                return False
            current_dict = current_dict[c]
        return "END" in current_dict

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        current_dict = self.trie
        for c in prefix:
            if c not in current_dict:
                return False
            current_dict = current_dict[c]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
if __name__ == '__main__':
    s = Trie()
    s.insert("apple")
    s.search("apple")
    s.startsWith("app")
    s.insert("app")
    s.search("app")
