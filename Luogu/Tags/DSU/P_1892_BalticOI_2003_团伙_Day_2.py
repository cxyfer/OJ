# fmt: off
import sys
it = iter(sys.stdin.read().split())
def input():
    return next(it)
# fmt: on


class UnionFind:
    __slots__ = ["n", "pa", "sz", "cnt"]

    def __init__(self, n: int):
        self.n = n
        self.pa = list(range(n))  # 父節點
        self.sz = [1] * n  # 連通分量大小
        self.cnt = n  # 連通分量數量

    def find(self, x: int) -> int:
        while self.pa[x] != x:
            self.pa[x] = self.pa[self.pa[x]]
            x = self.pa[x]
        return x

    def union(self, x: int, y: int) -> bool:
        fx, fy = self.find(x), self.find(y)
        if fx == fy:
            return False
        if self.sz[fx] < self.sz[fy]:
            fx, fy = fy, fx
        self.pa[fy] = fx
        self.sz[fx] += self.sz[fy]
        self.cnt -= 1
        return True


def solve():
    n = int(input())
    m = int(input())

    uf = UnionFind(n + 1)
    enemy = [0] * (n + 1)
    for _ in range(m):
        op, a, b = input(), input(), input()
        a, b = int(a), int(b)
        if op == "F":
            uf.union(a, b)
        else:
            # 敵人的敵人就是朋友
            if enemy[a] != 0:
                uf.union(b, enemy[a])
            if enemy[b] != 0:
                uf.union(a, enemy[b])
            # 更新敵人
            enemy[a], enemy[b] = b, a
    print(uf.cnt - 1)


if __name__ == "__main__":
    solve()
