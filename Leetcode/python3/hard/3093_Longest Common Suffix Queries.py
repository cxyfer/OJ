#
# @lc app=leetcode id=3093 lang=python3
#
# [3093] Longest Common Suffix Queries
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class TrieNode:
    __slot__ = ["child", "idx"]

    def __init__(self, idx=0):
        self.child = [None] * 26
        self.idx = idx


class Solution:
    def stringIndices(self, words: List[str], wordsQuery: List[str]) -> List[int]:
        root = TrieNode()
        for i, word in enumerate(words):
            node = root
            ln = len(word)
            if ln < len(words[node.idx]):
                node.idx = i
            for ch in reversed(word):
                c = ord(ch) - ord("a")
                if node.child[c] is None:
                    node.child[c] = TrieNode(idx=i)
                node = node.child[c]
                if ln < len(words[node.idx]):
                    node.idx = i

        ans = []
        for word in wordsQuery:
            node = root
            for ch in reversed(word):
                c = ord(ch) - ord("a")
                if node.child[c] is None:
                    break
                node = node.child[c]
            ans.append(node.idx)
        return ans
# @lc code=end

