"""
P4052 [JSOI2007] 文本生成器
https://www.luogu.com.cn/problem/P4052
"""
from collections import deque, defaultdict

class Node:
    def __init__(self):
        self.child = [None] * 26
        self.fail = None  # fail pointer
        self.last = None  # suffix link，用來快速跳到一定是某個 word 結尾的節點
        self.length = 0  # 可以取代 is_end 和 depth

class AhoCorasick:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str):
        node = self.root
        for ch in word: 
            idx = ord(ch) - ord('A')
            if not node.child[idx]:
                node.child[idx] = Node()
            node = node.child[idx]
        node.length = len(word)

    def build(self):
        self.root.fail = self.root.last = self.root
        # BFS
        q = deque()
        for i, v in enumerate(self.root.child):
            if v is None:  
                self.root.child[i] = self.root  # 添加虛擬子節點
            else:
                v.fail = v.last = self.root
                q.append(v)
        while q:
            u = q.popleft()
            for i, v in enumerate(u.child):
                if v is None:
                    u.child[i] = u.fail.child[i]  # 添加虛擬子節點
                else:
                    v.fail = u.fail.child[i]  # 失配位置
                    v.last = v.fail if v.fail.length else v.fail.last  # 上一個一定是某個 word 結尾的節點
                    q.append(v)

MOD = int(1e4 + 7)

def solve():
    n, m = map(int, input().split())
    words = [input().strip() for _ in range(n)]

    ac = AhoCorasick()
    for word in words:
        ac.insert(word)
    ac.build()

    # f[i][u] 表示長度為 i 的字串中，最後停在 u 節點，且不包含 words 中的單字的字串數量
    f = [defaultdict(int) for _ in range(m + 1)]
    f[0][ac.root] = 1
    for i in range(m):
        for u in f[i]:
            for v in u.child:
                # 如果 v.length > 0 或 v.last != ac.root，則到達 v 時會包含 words 中的字串，不能轉移過去
                if v is not None and v.length == 0 and v.last == ac.root:
                    f[i + 1][v] += f[i][u]
                    f[i + 1][v] %= MOD
    print((pow(26, m, MOD) - sum(f[m].values())) % MOD)

if __name__ == "__main__":
    solve()