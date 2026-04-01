from typing import Optional


class WeightedDSU:
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
            self.dis[x] %= 3
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
            return (dy - dx) % 3 == w

        if self.sz[rx] < self.sz[ry]:  # fa[rx] = ry
            # rx <------- ry
            # |           |
            # | dx        | dy
            # ↓           ↓
            # x --------> y   (約束 w = pot(y) - pot(x))
            # => pot(rx) - pot(ry) = dy - w - dx
            self.fa[rx] = ry
            self.dis[rx] = (dy - w - dx) % 3
            self.sz[ry] += self.sz[rx]
        else:  # fa[ry] = rx
            # rx -------> ry
            # |           |
            # | dx        | dy
            # ↓           ↓
            # x --------> y   (約束 w = pot(y) - pot(x))
            # => pot(ry) - pot(rx) = w - dy + dx
            self.fa[ry] = rx
            self.dis[ry] = (w - dy + dx) % 3
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
        return (self.potential(y) - self.potential(x)) % 3


def solve():
    n, k = map(int, input().split())
    uf = WeightedDSU(n + 1)
    ans = 0
    for _ in range(k):
        op, x, y = map(int, input().split())
        # 超出範圍或自己吃自己必假
        if x < 1 or x > n or y < 1 or y > n or op == 2 and x == y:
            ans += 1
            continue
        w = 0 if op == 1 else 1  # 同類:0 ； x 吃 y:1
        if not uf.union(x, y, w):
            ans += 1
    print(ans)


if __name__ == "__main__":
    solve()
