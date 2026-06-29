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
        self.cnt = 0


class AhoCorasick:
    def __init__(self):
        self.root = Node()
        self.nodes = []

    def insert(self, word: str):
        node = self.root
        for ch in word:
            c = ord(ch) - ord("a")
            if not node.child[c]:
                node.child[c] = Node()
            node = node.child[c]
        node.length = len(word)
        self.nodes.append(node)

    def build(self):  # O(|Σ|N)，N 是節點數；若 |Σ|=26 視為常數，則為 O(N) = O(L)
        self.root.fail = self.root.last = self.root
        # BFS
        q = deque()
        order = []
        for i, v in enumerate(self.root.child):
            if v is None:
                # 添加虛擬子節點
                self.root.child[i] = self.root
            else:
                v.fail = v.last = self.root
                q.append(v)
                order.append(v)
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
                    order.append(v)
        self.order = order


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
        c = ord(ch) - ord("a")
        node = node.child[c]
        node.cnt += 1

    for node in reversed(ac.order):
        node.fail.cnt += node.cnt

    for node in ac.nodes:
        print(node.cnt)


if __name__ == "__main__":
    solve()
