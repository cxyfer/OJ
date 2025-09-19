"""
P3808 AC 自动机（简单版）
https://www.luogu.com.cn/problem/P3808
Python TLE, C++ AC
"""
import sys
from collections import deque

it = iter(sys.stdin.read().splitlines())
input = lambda: next(it)

class Node:
    def __init__(self):
        self.child = [None] * 26
        self.fail = None  # fail pointer
        self.cnt = 0

class AhoCorasick:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str):
        node = self.root
        for ch in word: 
            idx = ord(ch) - ord('a')
            if not node.child[idx]:
                node.child[idx] = Node()
            node = node.child[idx]
        node.cnt += 1

    def build(self):
        self.root.fail = self.root
        # BFS
        q = deque()
        for v in self.root.child:
            if v is None: continue
            v.fail = self.root
            q.append(v)
        while q:
            u = q.popleft()
            for i, v in enumerate(u.child):
                if v is None: continue
                fu = u.fail
                while fu != self.root and fu.child[i] is None:
                    fu = fu.fail
                if fu.child[i] is not None:
                    v.fail = fu.child[i]
                else: # 如果一路找到根節點都沒有，則 fail 指向根
                    v.fail = self.root
                q.append(v)

def solve():
    n = int(input().strip())
    words = [input().strip() for _ in range(n)]
    t = input().strip()

    ac = AhoCorasick()
    for word in words:
        ac.insert(word)
    ac.build()

    ans = 0
    node = ac.root
    for ch in t:
        idx = ord(ch) - ord('a')
        while node != ac.root and node.child[idx] is None:
            node = node.fail
        if node.child[idx] is not None:
            node = node.child[idx]
        if node.cnt > 0:
            ans += node.cnt
            node.cnt = 0
    print(ans)

if __name__ == "__main__":
    solve()