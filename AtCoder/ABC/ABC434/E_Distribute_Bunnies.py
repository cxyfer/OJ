class UnionFind:
    __slots__ = ["n", "pa", "sz", "cnt"]

    def __init__(self, n: int):
        self.n = n
        self.pa = list(range(n))  # 父節點
        self.sz = [1] * n  # 連通分量包含的點數
        self.cnt = [0] * n  # 連通分量包含的邊數

    def find(self, x: int) -> int:
        while self.pa[x] != x:
            self.pa[x] = self.pa[self.pa[x]]
            x = self.pa[x]
        return x

    def union(self, x: int, y: int) -> None:
        fx, fy = self.find(x), self.find(y)
        self.cnt[fx] += 1
        if fx == fy:
            return
        if self.sz[fx] < self.sz[fy]:
            fx, fy = fy, fx
        self.pa[fy] = fx
        self.sz[fx] += self.sz[fy]
        self.cnt[fx] += self.cnt[fy]


def solve():
    N = int(input())
    rabbits = [tuple(map(int, input().split())) for _ in range(N)]

    Xs = set()
    for x, r in rabbits:
        Xs.add(x - r)
        Xs.add(x + r)
    Xs = sorted(list(Xs))
    mp = {x: i for i, x in enumerate(Xs)}

    uf = UnionFind(len(Xs))
    for x, r in rabbits:
        uf.union(mp[x - r], mp[x + r])

    ans = 0
    for u in range(len(Xs)):
        if uf.find(u) == u:
            ans += min(uf.sz[u], uf.cnt[u])
    print(ans)


if __name__ == "__main__":
    solve()
