class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # so that i can recursively check with a starting root node and check if each square has any characters belonging to the children of that root.
        root = self.createTrie(words) # call rec on every indice, instantiating an empty tring but append words to a words each time. return words.
        self.words = []
        for row in range(len(board)):
            for col in range(len(board[0])):
                string = ""
                self.rec(root, board, (row,col), string, set())
        self.words = set(self.words)
        return list(self.words)

    def rec(self, root, board, indices, string, visited): 
        char = board[indices[0]][indices[1]]
        if char not in root.children:
            return 
        
        string += char
        node = root.children[char]
        if node.isFinished:
            self.words.append(string)
        visited.add(indices)
        nextIndices = self.getValidIndices(indices, board)
        for indice in nextIndices:
            if indice in visited:
                continue
            self.rec(node, board, indice, string, visited)
        visited.remove(indices)

    def createTrie(self, words):
        root = TrieNode()
        for word in words:
            curr = root
            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
            curr.isFinished = True
        return root

    def getValidIndices(self, indices, board) -> List[Tuple[int, int]]:
        numRows = len(board)
        numCols = len(board[0])
        row, col = indices 
        res = []

        if row != 0:
            res.append((row-1, col)) # up

        if row + 1 != numRows:
            res.append((row+1, col)) # down

        if col != 0:
            res.append((row, col-1)) # left
        
        if col + 1 != numCols:
            res.append((row, col+1)) # right
        return res

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isFinished = False