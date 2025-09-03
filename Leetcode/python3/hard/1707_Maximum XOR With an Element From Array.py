#
# @lc app=leetcode id=1707 lang=python3
#
# [1707] Maximum XOR With an Element From Array
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class TrieNode:
    __slots__ = ['child', 'min_val']
    def __init__(self):
        self.child = [None, None]
        self.min_val = float('inf')

class Trie:
    def __init__(self, B=30):
        self.root = TrieNode()
        self.B = B

    def insert(self, x: int):
        node = self.root
        node.min_val = min(node.min_val, x)
        for k in range(self.B, -1, -1):
            b = (x >> k) & 1
            if node.child[b] is None:
                node.child[b] = TrieNode()
            node = node.child[b]
            node.min_val = min(node.min_val, x)

    def max_xor(self, x: int, m: int) -> int:
        node = self.root
        if node.min_val > m:
            return -1
        res = 0
        for k in range(self.B, -1, -1):
            b = (x >> k) & 1
            if node.child[b ^ 1] is not None and node.child[b ^ 1].min_val <= m:
                res |= (1 << k)
                node = node.child[b ^ 1]
            else:
                node = node.child[b]
        return res

class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        trie = Trie()
        for x in nums:
            trie.insert(x)
        return [trie.max_xor(x, m) for x, m in queries]
# @lc code=end