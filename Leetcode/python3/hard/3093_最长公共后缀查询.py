#
# @lc app=leetcode.cn id=3093 lang=python3
#
# [3093] 最长公共后缀查询
#
from preImport import *
# @lc code=start

class Node: # Trie
    def __init__(self):
        self.child = [None] * 26
        self.min_l = float('inf') # min length of the word in the subtree
        self.index = -1 # index of the word in the wordsContainer

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        root = Node()
        for idx, word in enumerate(wordsContainer): # build trie
            n = len(word)
            cur = root
            if n < cur.min_l: # for root node
                cur.min_l = n
                cur.index = idx
            for ch in word[::-1]:
                ch = ord(ch) - ord('a')
                if not cur.child[ch]:
                    cur.child[ch] = Node()
                cur = cur.child[ch]
                if n < cur.min_l:
                    cur.min_l = n
                    cur.index = idx
        ans = []
        for word in wordsQuery: # query
            cur = root
            for ch in word[::-1]:
                ch = ord(ch) - ord('a')
                if not cur.child[ch]:
                    break
                cur = cur.child[ch]
            ans.append(cur.index)
        return ans
# @lc code=end

