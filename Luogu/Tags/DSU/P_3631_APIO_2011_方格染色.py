from typing import Optional

"""
將紅色以 1 表示，藍色以 0 表示。
令 f(i, j) 表示左上角為 (i, j) 的 2x2 矩形中，顏色之異或值。
f(i, j) = A[i][j] ^ A[i+1][j] ^ A[i][j+1] ^ A[i+1][j+1]
根據題目要求，需滿足 f(i, j) = 1。

將這個約束擴展到左上角為 (1, 1) 右下角為 (x, y) 的矩形中，
XOR(f(i, j) for i in range(1, x) for j in range(1, y)) = XOR(1 for i in range(1, x) for j in range(1, y))
又以 (1, 1) 為左上角，(x, y) 為右下角的矩形中，包含了 (x - 1) * (y - 1) 個 2x2 矩形，
因此右式 = (x - 1) * (y - 1) & 1
而左式中，中心的格子都被計算了四次，邊界非角落的格子都被計算了兩次，角落的格子只被計算了一次，
因此左式 = A[1][1] ^ A[1][y] ^ A[x][1] ^ A[x][y]
得到約束 A[1][1] ^ A[1][y] ^ A[x][1] ^ A[x][y] = (x - 1) * (y - 1) & 1
移項得到 A[x][y] = A[1][1] ^ A[1][y] ^ A[x][1] ^ ((x - 1) * (y - 1) & 1)

令 R[x] = A[1][x], C[y] = A[y][1],
則可以枚舉 A[1][1] 是 0 或 1，將約束轉換為 R[x] ^ C[y] = A[1][1] ^ A[x][y] ^ ((x - 1) * (y - 1) & 1)
那麼可以用 n + m 個點分別表示 R[x] 和 C[y]，並用帶權並查集維護 R[x] ^ C[y] 的關係。
初始時 R[1] ^ C[1] = 0。

最終對於除了 A[1][1] 之外的每一個連通分量，都有 2 種選擇，因此答案為 2^(連通分量數 - 1)
"""


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
        w %= 2
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

    def same(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def diff(self, x: int, y: int) -> Optional[int]:
        """
        若同集合，回傳 potential(y) - potential(x)，否則回傳 None
        """
        if not self.same(x, y):
            return None
        return self.potential(y) - self.potential(x)


MOD = int(1e9)  # ?????


def solve():
    n, m, k = map(int, input().split())
    N = n + m + 1

    constraints = []
    for _ in range(k):
        x, y, c = map(int, input().split())
        constraints.append((x, y, c))

    ans = 0
    for a in (0, 1):  # 枚舉 A[1][1] 是 0 或 1
        uf = WeightedDSU(N)
        uf.union(1, n + 1, 0)  # 約束: R[1] ^ C[1] = 0
        for x, y, c in constraints:
            w = c ^ ((x - 1) * (y - 1) & 1) ^ a
            if not uf.union(x, n + y, w):
                break
        else:
            comps = sum(1 for u in range(1, N) if uf.find(u) == u)
            ans += pow(2, comps - 1, MOD) % MOD
            ans %= MOD

    print(ans)


if __name__ == "__main__":
    solve()
