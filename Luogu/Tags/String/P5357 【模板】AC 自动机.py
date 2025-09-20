import sys
from collections import deque

it = iter(sys.stdin.read().splitlines())
input = lambda: next(it)

class Node:
    def __init__(self):
        self.child = [None] * 26
        self.fail = None  # fail pointer
        self.last = None  # suffix link，用來快速跳到一定是某個 word 結尾的節點
        self.length = 0
        self.cnt = 0

class AhoCorasick:
    def __init__(self):
        self.root = Node()
        self.pos = []
        self.order = []

    def insert(self, word: str):
        node = self.root
        for ch in word: 
            idx = ord(ch) - ord('a')
            if not node.child[idx]:
                node.child[idx] = Node()
            node = node.child[idx]
        node.length = len(word)
        self.pos.append(node)

    def build(self):  # O(|Σ|)，|Σ| 是字元集大小，n 是節點數，適合較稠密的 Trie 
        self.root.fail = self.root.last = self.root
        # BFS
        q = deque()
        for i, v in enumerate(self.root.child):
            if v is None:  
                self.root.child[i] = self.root  # 添加虛擬子節點
            else:
                v.fail = v.last = self.root
                q.append(v)
                self.order.append(v)
        while q:
            u = q.popleft()
            for i, v in enumerate(u.child):
                if v is None:
                    u.child[i] = u.fail.child[i]  # 添加虛擬子節點
                else:
                    v.fail = u.fail.child[i]  # 失配位置
                    v.last = v.fail if v.fail.length else v.fail.last  # 上一個一定是某個 word 結尾的節點
                    q.append(v)
                    self.order.append(v)

def solve():
    n = int(input().strip())
    words = [input().strip() for _ in range(n)]
    t = input().strip()

    ac = AhoCorasick()
    for word in words:
        ac.insert(word)
    ac.build()

    node = ac.root
    for ch in t:
        idx = ord(ch) - ord('a')
        while node != ac.root and node.child[idx] is None:
            node = node.fail
        if node.child[idx] is not None:
            node = node.child[idx]
        node.cnt += 1

    for node in reversed(ac.order):
        node.fail.cnt += node.cnt

    for node in ac.pos:
        print(node.cnt)

if __name__ == "__main__":
    solve()