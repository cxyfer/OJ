class UnionFind:
    __slots__ = ['n', 'pa']

    def __init__(self, n: int):
        self.n = n
        self.pa = list(range(n)) # 父節點

    def find(self, x: int) -> int:
        while self.pa[x] != x:
            self.pa[x] = self.pa[self.pa[x]]
            x = self.pa[x]
        return x

    def union(self, x: int, y: int) -> bool:
        fx, fy = self.find(x), self.find(y)
        if fx == fy:
            return False
        self.pa[fx] = fy
        return True

def calc(x):
    res = 0
    while x:
        res += x % 10
        x //= 10
    return res

t = int(input())

for _ in range(t):
    n, q = map(int, input().split())
    A = list(map(int, input().split()))
    uf = UnionFind(n + 1)
    for _ in range(q):
        op, *args = map(int, input().split())
        if op == 1:
            l, r = map(lambda x : x - 1, args)
            idx = uf.find(l)
            while (idx <= r):
                A[idx] = calc(A[idx])
                if A[idx] < 10:
                    uf.union(idx, idx + 1)  # 向右合併
                idx = uf.find(idx + 1)
        else:
            idx = args[0] - 1
            print(A[idx])