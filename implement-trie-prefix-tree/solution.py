class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # can replace indexing for "char in word"
        curr = self.root
        for i in range(len(word)):
            if word[i] not in curr.children:
                curr.children[word[i]] = TrieNode()
            curr = curr.children.get(word[i], False)
        curr.children["."] = True

    def search(self, word: str) -> bool:
        curr = self.root
        length = len(word)
        
        for i in range(0, length):
            if word[i] in curr.children:
                curr = curr.children[word[i]]
            else:
                return False
        else:
            if curr.children.get(".", False):
                return True
            return False

    def startsWith(self, prefix: str) -> bool:
        # traverse tree
        curr = self.root 
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        else:
            return True

    def compareWords(self, word1, word2) -> str:
        if word1 == word2:
            return word1
        for charIndex in range(min(len(word1), len(word2))):
            if word1[charIndex] > word2[charIndex]:
                return word1
            elif word1[charIndex] < word2[charIndex]:
                return word2
            else:
                continue
        return word1
        
class TrieNode:
    def __init__(self):
        self.children = {}


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)