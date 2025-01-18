# @algorithm @lc id=208 lang=python3 
# @title implement-trie-prefix-tree
class Trie:

    def __init__(self):
        self.isEnd = False # whether the word is end or not
        self.child = [None] * 26

    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            idx = ord(ch) - ord('a')
            if not node.child[idx]:
                node.child[idx] = Trie()
            node = node.child[idx] # last node
        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self
        for ch in word:
            idx = ord(ch) - ord('a')
            if not node.child[idx]:
                return False
            node = node.child[idx]
        return node.isEnd

    def startsWith(self, prefix: str) -> bool:
        node = self
        for ch in prefix:
            idx = ord(ch) - ord('a')
            if not node.child[idx]:
                return False
            node = node.child[idx]
        return True