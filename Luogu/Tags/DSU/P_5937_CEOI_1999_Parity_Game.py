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
            self.dis[x] %= 2
            fa[x] = rt
        return fa[x]

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
            return (dy - dx) % 2 == w

        if self.sz[rx] < self.sz[ry]:  # fa[rx] = ry
            # rx <------- ry
            # |           |
            # | dx        | dy
            # ↓           ↓
            # x --------> y
            # => pot(rx) - pot(ry) = dy - w - dx
            self.fa[rx] = ry
            self.dis[rx] = (dy - w - dx) % 2
            self.sz[ry] += self.sz[rx]
        else:  # fa[ry] = rx
            # rx -------> ry
            # |           |
            # | dx        | dy
            # ↓     w     ↓
            # x --------> y
            # => pot(ry) - pot(rx) = w - dy + dx
            self.fa[ry] = rx
            self.dis[ry] = (w - dy + dx) % 2
            self.sz[rx] += self.sz[ry]

        return True

def solve():
    n = int(input())
    m = int(input())

    Xs = set()
    constraints = []
    for _ in range(m):
        l, r, p = input().split()
        l, r = int(l), int(r)
        Xs.add(l)
        Xs.add(r + 1)
        constraints.append((l, r, 1 if p == "odd" else 0))

    n = len(Xs)
    Xs = sorted(Xs)
    mp = {x: i for i, x in enumerate(Xs)}

    uf = WeightedDSU(n)
    for i, (l, r, p) in enumerate(constraints):
        l, r = mp[l], mp[r + 1]
        if not uf.union(l, r, p):
            print(i)
            break
    else:
        print(m)

if __name__ == "__main__":
    solve()