from collections import deque

MOD = 998244353


class Node:
    def __init__(self):
        self.child = [None] * 26
        self.fail = None  # fail pointer
        self.last = None  # suffix link，用來快速跳到一定是某個 word 結尾的節點
        self.length = 0  # 可以取代 is_end 和 depth
        self.id = -1


class AhoCorasick:
    def __init__(self):
        self.root = Node()
        self.root.id = 0
        self.nodes = [self.root]  # 保留所有節點

    def insert(self, word: str):
        node = self.root
        for ch in word:
            c = ord(ch) - ord("a")
            if not node.child[c]:
                node.child[c] = Node()
                node.child[c].id = len(self.nodes)
                self.nodes.append(node.child[c])
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


class Matrix:
    def __init__(self, mat):
        self.mat = mat

    def __mul__(self, other):
        A, B = self.mat, other.mat
        assert len(A[0]) == len(B)
        n, p, m = len(A), len(B), len(B[0])
        res = [[0] * m for _ in range(n)]
        for i in range(n):
            ri = res[i]
            Ai = A[i]
            for k in range(p):
                if Ai[k] == 0:
                    continue
                x = Ai[k]
                Bk = B[k]
                for j in range(m):
                    ri[j] = (ri[j] + x * Bk[j]) % MOD
        return Matrix(res)

    def __pow__(self, k):
        assert len(self.mat) == len(self.mat[0])
        n = len(self.mat)
        res = Matrix([[int(i == j) for j in range(n)] for i in range(n)])
        base = self
        while k > 0:
            if k & 1:
                res *= base
            base *= base
            k >>= 1
        return res

    def mul_pow(self, k, x):
        assert len(self.mat[0]) == len(x.mat)
        res = x
        base = self
        while k > 0:
            if k & 1:
                res = base * res
            base *= base
            k >>= 1
        return res

    def __getitem__(self, i):
        return self.mat[i]

    def __str__(self):
        return "\n".join(map(lambda x: " ".join(map(str, x)), self.mat))


def solve():
    n, k = map(int, input().split())

    ac = AhoCorasick()
    for _ in range(k):
        ac.insert(input().strip())
    ac.build()

    nodes = ac.nodes
    m = len(nodes)

    bad = [False] * m
    for node in nodes:
        if node.length > 0 or node.last != ac.root:
            bad[node.id] = True

    # T[v][u] 表示從 u 狀態加入一個字元後，到達 v 狀態的方案數
    T = [[0] * m for _ in range(m)]
    for u in nodes:
        if bad[u.id]:
            continue
        for v in u.child:
            if bad[v.id]:
                continue
            T[v.id][u.id] += 1

    T = Matrix(T)
    f = Matrix([[1] if i == 0 else [0] for i in range(m)])
    f = T.mul_pow(n, f)

    ans = sum(f[i][0] for i in range(m) if not bad[i]) % MOD
    print(ans)


if __name__ == "__main__":
    solve()
