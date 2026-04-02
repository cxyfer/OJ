from typing import Optional


class DSU:
    """
    帶權並查集
    維護條件：potential(y) - potential(x) = w

    支援：
    - union(x, y, w): 合併並加入約束 y - x = w
    - diff(x, y): 若同集合，回傳 y - x；否則回傳 None
    """

    def __init__(self, n: int):
        self.n = n
        self.fa = list(range(n))
        self.sz = [1] * n
        # dis[x] = potential(x) - potential(fa[x])
        self.dis = [0] * n

    def find(self, x: int) -> int:
        """回傳 x 的根，同時做路徑壓縮並更新 dis[x] 為 x 到根的位勢差。"""
        fa = self.fa
        if fa[x] != x:
            rt = self.find(fa[x])
            self.dis[x] += self.dis[fa[x]]
            fa[x] = rt
        return fa[x]

    def potential(self, x: int) -> int:
        """回傳 potential(x) - potential(fa[x])"""
        self.find(x)
        return self.dis[x]

    def union(self, x: int, y: int, w: int) -> bool:
        """
        合併並加入約束：potential(y) - potential(x) = w
        回傳：
        - True：成功合併（或已同集合且不發生矛盾）
        - False：已同集合但發生矛盾
        """
        rx, ry = self.find(x), self.find(y)
        dx, dy = self.dis[x], self.dis[y]
        if rx == ry:
            # x 和 y 在同一集合，不做合併
            return (dy - dx) == w

        if self.sz[rx] < self.sz[ry]:  # fa[rx] = ry
            # rx <------- ry
            # |           |
            # | dx        | dy
            # ↓           ↓
            # x --------> y
            # => pot(rx) - pot(ry) = dy - w - dx
            self.fa[rx] = ry
            self.dis[rx] = dy - w - dx
            self.sz[ry] += self.sz[rx]
        else:  # fa[ry] = rx
            # rx -------> ry
            # |           |
            # | dx        | dy
            # ↓     w     ↓
            # x --------> y
            # => pot(ry) - pot(rx) = w - dy + dx
            self.fa[ry] = rx
            self.dis[ry] = w - dy + dx
            self.sz[rx] += self.sz[ry]

        return True

    def same(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def diff(self, x: int, y: int) -> Optional[int]:
        """
        若同集合，回傳 potential(y) - potential(x)，否則回傳 None
        """
        if not self.same(x, y):
            return None
        return self.potential(y) - self.potential(x)


def solve():
    n, m = map(int, input().split())
    uf = DSU(n + 2)
    for _ in range(m):
        l, r, s = map(int, input().split())
        if not uf.union(l, r + 1, s):
            print("false")
            return
    print("true")


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()
