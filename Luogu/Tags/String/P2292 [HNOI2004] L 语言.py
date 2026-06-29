"""
P2292 [HNOI2004] L 语言
https://www.luogu.com.cn/problem/P2292
AC自動機優化DP

f[i] 表示 target[..i] 的後綴能否被 words 中的字串覆蓋，若能覆蓋則 f[i] = True，否則 f[i] = False。
f[i] = f[i - len(word)]，其中 word 是 words 中的字串

注意關鍵剪枝：
1. 當前需要長度至少為 i - ans 的模式串才能匹配，但不能超過 max_len
2. 在沿著 last 往上尋找的過程中，已經匹配 (f[i] == True) 就沒必要再往上找了

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
        self.length = 0  # 可以取代 is_end 和 depth


class AhoCorasick:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str):
        node = self.root
        for ch in word:
            c = ord(ch) - ord("a")
            if not node.child[c]:
                node.child[c] = Node()
            node = node.child[c]
        node.length = len(word)

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


def solve():
    n, q = map(int, input().split())

    ac = AhoCorasick()
    max_len = 0
    for _ in range(n):
        pattern = input().strip()
        ac.insert(pattern)
        max_len = max(max_len, len(pattern))
    ac.build()

    for _ in range(q):
        t = input().strip()
        m = len(t)

        ans = 0
        f = [False] * (m + 1)
        f[0] = True

        node = ac.root
        for i, ch in enumerate(t, 1):
            # 剪枝：當前需要長度至少為 i - ans 的模式串才能匹配，但不能超過 max_len
            if i - ans > max_len:
                break

            c = ord(ch) - ord("a")
            node = node.child[c]

            # 沒有任何字串的前綴與 t[..i] 的後綴匹配
            if node is ac.root:
                break

            # 沿著 last 往上尋找
            temp = node
            while temp is not ac.root:
                f[i] |= f[i - temp.length]
                # 剪枝：已經匹配就沒必要再往上找了
                if f[i]:
                    ans = i
                    break
                temp = temp.last
        print(ans)


if __name__ == "__main__":
    solve()
