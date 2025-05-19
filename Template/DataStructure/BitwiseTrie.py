"""
Bitwise Trie

Example:
- CSES-1655 Maximum Xor Subarray
"""

class TrieNode:
    __slots__ = ['ch']
    def __init__(self):
        self.ch = [None, None]

class BitwiseTrie:
    def __init__(self, bitlen=30):
        self.root = TrieNode()
        self.B = bitlen

    def insert(self, x: int):
        node = self.root
        for k in range(self.B, -1, -1):
            b = (x >> k) & 1
            if node.ch[b] is None:
                node.ch[b] = TrieNode()
            node = node.ch[b]

    def max_xor(self, x: int) -> int:
        node = self.root
        res = 0
        for k in range(self.B, -1, -1):
            b = (x >> k) & 1
            if node.ch[b ^ 1] is not None:
                res |= (1 << k)
                node = node.ch[b ^ 1]
            else:
                node = node.ch[b]
        return res