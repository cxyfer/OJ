#
# @lc app=leetcode id=1804 lang=python3
# @lcpr version=30204
#
# [1804] Implement Trie II (Prefix Tree)
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class TrieNode:
    def __init__(self):
        self.child = [None] * 26
        self.cnt = 0
        self.prefix_cnt = 0

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if node.child[idx] is None:
                node.child[idx] = TrieNode()
            node = node.child[idx]
            node.prefix_cnt += 1
        node.cnt += 1

    def countWordsEqualTo(self, word: str) -> int:
        node = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if node.child[idx] is None:
                return 0
            node = node.child[idx]
        return node.cnt

    def countWordsStartingWith(self, prefix: str) -> int:
        node = self.root
        for ch in prefix:
            idx = ord(ch) - ord('a')
            if node.child[idx] is None:
                return 0
            node = node.child[idx]
        return node.prefix_cnt

    def erase(self, word: str) -> None:
        node = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if node.child[idx] is None:
                return
            node = node.child[idx]
            node.prefix_cnt -= 1
        node.cnt -= 1

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)
# @lc code=end



