import sys
input = sys.stdin.readline

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

n = int(input())
A = list(map(int, input().split()))

trie = BitwiseTrie(bitlen=30)
trie.insert(0)

ans = s = 0
for x in A:
    s ^= x
    ans = max(ans, trie.max_xor(s))
    trie.insert(s)
print(ans)