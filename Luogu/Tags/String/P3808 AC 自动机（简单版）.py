"""
P3808 AC 自动机（简单版）
https://www.luogu.com.cn/problem/P3808
Python TLE, C++ AC
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

ALPH = 26


class Node:
    def __init__(self):
        self.child = [None] * ALPH
        self.fail = None
        self.cnt = 0


class AhoCorasick:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        node = self.root
        for ch in word:
            c = ord(ch) - ord("a")
            if node.child[c] is None:
                node.child[c] = Node()
            node = node.child[c]
        node.cnt += 1

    def build(self):
        self.root.fail = self.root

        q = deque()
        for i in range(ALPH):
            if self.root.child[i] is None:
                self.root.child[i] = self.root
            else:
                self.root.child[i].fail = self.root
                q.append(self.root.child[i])
        while q:
            u = q.popleft()
            for i in range(ALPH):
                if u.child[i] is None:
                    u.child[i] = u.fail.child[i]
                else:
                    v = u.child[i]
                    v.fail = u.fail.child[i]
                    q.append(v)


def solve():
    n = int(input())
    patterns = [input() for _ in range(n)]
    word = input()

    ac = AhoCorasick()
    for pattern in patterns:
        ac.insert(pattern)
    ac.build()

    ans = 0
    node = ac.root
    for ch in word:
        # 由於是 Trie 圖，直接轉移即可
        c = ord(ch) - ord("a")
        node = node.child[c]

        # 沿著 fail 鏈向上搜集所有匹配的模式串
        temp = node
        while temp is not ac.root and temp.cnt != -1:
            ans += temp.cnt
            # 標記為 -1，代表此節點已被統計過，避免重複計算
            temp.cnt = -1
            temp = temp.fail
    print(ans)


if __name__ == "__main__":
    solve()
