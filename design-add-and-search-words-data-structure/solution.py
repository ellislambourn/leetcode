class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.isFinished = True
           
    def search(self, word: str) -> bool:
        def subTreeSearch(word, node) -> bool:
            curr = node

            if word == "":
                return node.isFinished
            
            for i in range(len(word)):
                if word[i] == ".":
                    return any(subTreeSearch(word[i+1:], child) for child in curr.children.values())

                if word[i] not in curr.children:
                    return False

                curr = curr.children[word[i]]

            else: return curr.isFinished
        curr = self.root
        return subTreeSearch(word, curr)

        
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isFinished = False