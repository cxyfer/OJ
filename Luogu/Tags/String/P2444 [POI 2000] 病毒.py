import sys
from collections import deque

sys.setrecursionlimit(int(3e4))
it = iter(sys.stdin.read().splitlines())
input = lambda: next(it)

class Node:
    def __init__(self):
        self.child = [None] * 2
        self.fail = None  # fail pointer
        self.last = None  # suffix link，用來快速跳到一定是某個 word 結尾的節點
        self.length = 0  # 可以取代 is_end 和 depth
        self.vis = False
        self.ins = False  # 是否在 Stack 中

class AhoCorasick:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str):
        node = self.root
        for ch in word: 
            idx = ord(ch) - ord('0')
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

def solve():
    n = int(input())
    words = [input().strip() for _ in range(n)]
    ac = AhoCorasick()
    for word in words:
        ac.insert(word)
    ac.build()

    def dfs(u: Node) -> bool:
        u.vis = u.ins = True
        for v in u.child:
            if v is None: continue
            # 如果 v.length > 0 或 v.last != ac.root，則到達 v 時會包含 words 中的字串，不能轉移過去
            if v.length > 0 or v.last != ac.root: continue
            # DFS 判斷是否存在環
            if not v.vis:
                if dfs(v): return True
            elif v.ins:
                return True
        u.ins = False
        return False
    print("TAK" if dfs(ac.root) else "NIE")

if __name__ == "__main__":
    solve()