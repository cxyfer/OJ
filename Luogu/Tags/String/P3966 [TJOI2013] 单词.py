"""
P3966 [TJOI2013] 单词
https://www.luogu.com.cn/problem/P3966
"""
from collections import deque

class Node:
    def __init__(self):
        self.child = [None] * 26
        self.fail = None  # fail 指標
        self.cnt = 0

class AhoCorasick:
    def __init__(self):
        self.root = Node()
        self.pos = []  # 每個單字的最後一個字元對應的節點
        self.order = []  # BFS 順序，用於最後的計數匯總

    def insert(self, word: str):
        node = self.root
        for ch in word: 
            idx = ord(ch) - ord('a')
            if not node.child[idx]:
                node.child[idx] = Node()
            node = node.child[idx]
        self.pos.append(node)

    def traverse(self, word: str):
        node = self.root
        for ch in word: 
            idx = ord(ch) - ord('a')
            while node != self.root and node.child[idx] is None:
                node = node.fail
            if node.child[idx] is not None:
                node = node.child[idx]
            node.cnt += 1

    def build(self):
        self.root.fail = self.root
        q = deque()
        
        # BFS
        for v in self.root.child:
            if v is None: continue
            v.fail = self.root
            q.append(v)
            self.order.append(v)
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
                self.order.append(v)

def solve():
    n = int(input().strip())
    words = [input().strip() for _ in range(n)]

    ac = AhoCorasick()
    for word in words:
        ac.insert(word)
    ac.build()
    for word in words:
        ac.traverse(word)
    
    for u in reversed(ac.order):
        if u.fail is None: continue
        u.fail.cnt += u.cnt
    
    for u in ac.pos:
        print(u.cnt)

if __name__ == "__main__":
    solve()