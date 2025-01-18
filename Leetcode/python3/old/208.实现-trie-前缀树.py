#
# @lc app=leetcode.cn id=208 lang=python3
#
# [208] 实现 Trie (前缀树)
#

# @lc code=start
class Trie:
    def __init__(self):
        self.isEnd = False
        self.child = [None] * 26

    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            ch = ord(ch) - ord("a")
            if not node.child[ch]:
                node.child[ch] = Trie()
            node = node.child[ch]
        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self
        for ch in word:
            ch = ord(ch) - ord("a")
            if not node.child[ch]:
                return False
            node = node.child[ch]
        return node.isEnd

    def startsWith(self, prefix: str) -> bool:
        node = self
        for ch in prefix:
            ch = ord(ch) - ord("a")
            if not node.child[ch]:
                return False
            node = node.child[ch]
        return True 
# @lc code=end

obj = Trie()
obj.insert("abcde")
param_2 = obj.search("abcde")
param_3 = obj.startsWith("abc")