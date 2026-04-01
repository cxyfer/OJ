from typing import Optional


class DSU:
    def __init__(self, n: int):
        self.n = n
        self.fa = list(range(n))
        self.sz = [1] * n
        self.dis = [0] * n

    def find(self, x: int) -> int:
        fa = self.fa
        # if fa[x] != x:
        #     rt = self.find(fa[x])
        #     self.dis[x] += self.dis[fa[x]]
        #     fa[x] = rt
        # return fa[x]
        path = []
        curr = x
        while fa[curr] != curr:
            path.append(curr)
            curr = fa[curr]

        root = curr
        for node in reversed(path):
            self.dis[node] += self.dis[fa[node]]
            fa[node] = root
        return root

    def union(self, x: int, y: int) -> bool:
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return True
        # 讓 rx 掛在 ry 上，根據題意此時的 dis[rx] = sz[ry]
        self.fa[rx] = ry
        self.dis[rx] = self.sz[ry]
        self.sz[ry] += self.sz[rx]
        return True

    def same(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def diff(self, x: int, y: int) -> Optional[int]:
        if not self.same(x, y):
            return None
        return self.dis[x] - self.dis[y]


N = int(3e4)


def solve():
    t = int(input())
    uf = DSU(N + 1)
    for _ in range(t):
        op, x, y = input().split()
        x, y = int(x), int(y)
        if op == "M":
            uf.union(x, y)
        else:
            if uf.same(x, y):
                print(abs(uf.diff(x, y)) - 1)
            else:
                print(-1)


if __name__ == "__main__":
    solve()
