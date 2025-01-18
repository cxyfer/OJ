from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.child = {}
        self.idx = -1

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.cnt = 0

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.child:
                node.child[ch] = TrieNode()
            node = node.child[ch]
        if node.idx == -1:
            node.idx = self.cnt
            self.cnt += 1
        return node.idx
    
class UnionFind:
    def __init__(self, n):
        self.pa = list(range(n))
        self.sz = [1] * n
        self.cnt = n

    def find(self, x):
        if self.pa[x] != x:
            self.pa[x] = self.find(self.pa[x])
        return self.pa[x]
    
    def union(self, x, y):
        fx, fy = self.find(x), self.find(y)
        if fx == fy:
            return False
        if self.sz[fx] < self.sz[fy]:
            fx, fy = fy, fx
        self.pa[fy] = fx
        self.sz[fx] += self.sz[fy]
        self.cnt -= 1
        return True

edges = []
trie = Trie()
while True:
    try:
        u, v = input().strip().split()
        u = trie.insert(u)
        v = trie.insert(v)
        edges.append((u, v))
    except EOFError:
        break

n = trie.cnt
uf = UnionFind(n)
cnt = [0] * n
for i, (u, v) in enumerate(edges):
    cnt[u] += 1
    cnt[v] += 1
    uf.union(u, v)

cnt_odd = sum(1 for val in cnt if val & 1)
root = uf.find(edges[0][0]) if len(edges) else -1 # 避免 egdes 為空的情況
is_connected = all(uf.find(u) == root for u, _ in edges)
if (cnt_odd == 0 or cnt_odd == 2) and is_connected:
    print("Possible")
else:
    print("Impossible")