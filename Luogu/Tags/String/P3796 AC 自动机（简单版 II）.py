"""
P3796 AC 自动机（简单版 II）
https://www.luogu.com.cn/problem/P3796
Python MLE, C++ AC
"""

from collections import deque

# fmt: off
import sys
it = iter(sys.stdin.read().splitlines())
def input():
    return next(it)
def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)) + end)
# fmt: on


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

    def insert(self, word: str) -> Node:
        node = self.root
        for ch in word:
            c = ord(ch) - ord("a")
            if not node.child[c]:
                node.child[c] = Node()
            node = node.child[c]
        node.length = len(word)
        return node

    def build(self):  # O(|Σ|N)，N 是節點數；若 |Σ|=26 視為常數，則為 O(N) = O(L)
        self.root.fail = self.root.last = self.root
        # BFS
        q = deque()
        for i, v in enumerate(self.root.child):
            if v is None:
                # 添加虛擬子節點
                self.root.child[i] = self.root
            else:
                v.fail = v.last = self.root
                q.append(v)
        while q:
            u = q.popleft()
            for i, v in enumerate(u.child):
                if v is None:
                    # 添加虛擬子節點
                    u.child[i] = u.fail.child[i]
                else:
                    # 失配位置
                    v.fail = u.fail.child[i]
                    # 上一個一定是某個 word 結尾的節點
                    v.last = v.fail if v.fail.length else v.fail.last
                    q.append(v)


def solve(n):
    words = [input().strip() for _ in range(n)]
    t = input().strip()

    ac = AhoCorasick()
    nodes = []
    for word in words:
        nodes.append(ac.insert(word))
    ac.build()

    node = ac.root
    for ch in t:
        c = ord(ch) - ord("a")
        node = node.child[c]

        # 沿著 last 鏈向上搜集所有匹配的模式串
        temp = node
        while temp is not ac.root:
            temp.cnt += 1
            temp = temp.last

    mx = 0
    ans = []
    for node, word in zip(nodes, words):
        if node.cnt > mx:
            mx = node.cnt
            ans = [word]
        elif node.cnt == mx:
            ans.append(word)

    print(mx)
    for word in ans:
        print(word)


if __name__ == "__main__":
    while True:
        n = int(input().strip())
        if n == 0:
            break
        solve(n)
