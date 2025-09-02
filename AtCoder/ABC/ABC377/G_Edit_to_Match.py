class TrieNode:
    def __init__(self):
        self.child = [None] * 26
        self.dist = float('inf')
        self.is_end = False

    def insert(self, s):
        n = len(s)
        node = self
        node.dist = min(node.dist, n)
        for i, ch in enumerate(s):
            c = ord(ch) - ord('a')
            if not node.child[c]:
                node.child[c] = TrieNode()
            node = node.child[c]
            node.dist = min(node.dist, n - 1 - i)
        node.is_end = True
        return node
    
    def query(self, s):
        n = len(s)
        node = self
        res = len(s)
        for i, ch in enumerate(s):
            c = ord(ch) - ord('a')
            if not node.child[c]:
                break
            node = node.child[c]
            res = min(res, n - 1 - i + node.dist)
        return res

n = int(input())
S = [input() for _ in range(n)]

root = TrieNode()
for s in S:
    print(root.query(s))
    root.insert(s)