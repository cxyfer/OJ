"""
根據題意，cost(l, r) = ((r - l) + s[r + 1] - s[l] - L)^2，其中 s[i] 是 A 的前綴和。
可以得到轉移式：f[i] = min_{j < i} f[j] + ((i - (j + 1)) + s[i + 1] - s[j + 1] - L)^2

令 a[i] = i + s[i + 1], b[j] = j + s[j + 1] + L + 1，
則轉移式可以寫成 f[i] = min_{j < i} f[j] + (a[i] - b[j])^2
展開後得到 f[i] = min_{j < i} (f[j] + a[i]^2 - 2 * a[i] * b[j] + b[j]^2)，
把與 j 無關的 a[i]^2 提出來，得到 f[i] = a[i]^2 + min_{j < i} (f[j] + b[j]^2 - 2 * a[i] * b[j])，
令 p = (-2 * a[i], 1), vj = (b[j], f[j] + b[j]^2)，則可以使用 CHT 來維護 vj，查詢 min(p·vj)。
"""

from itertools import accumulate
from math import inf
from collections import deque


class Vec:
    __slots__ = "x", "y"

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __add__(self, b: "Vec") -> "Vec":
        return Vec(self.x + b.x, self.y + b.y)

    def __sub__(self, b: "Vec") -> "Vec":
        return Vec(self.x - b.x, self.y - b.y)

    def det(self, b: "Vec") -> int:
        return self.x * b.y - self.y * b.x

    def dot(self, b: "Vec") -> int:
        return self.x * b.x + self.y * b.y


class ConvexHull:
    """
    注意：
    - add() 的點需要依 x 遞增加入。
    - query_bisect() 不要求查詢向量單調，使用二分搜尋。
    - query_mono() 使用單調隊列優化，因此查詢向量 p 需要滿足最佳點索引單調往前移動。
    """

    def __init__(self):
        self.hull = deque()

    def add(self, v: Vec) -> None:
        hull = self.hull

        # 如果新點與最後一個點 x 相同，只保留對應 mode 下較優的 y
        if hull and hull[-1].x == v.x:
            if hull[-1].y <= v.y:
                return
            hull.pop()

        # 維護凸包性質，移除不可能成為凸包的中間點
        while len(hull) >= 2 and (hull[-1] - hull[-2]).det(v - hull[-1]) <= 0:
            hull.pop()

        hull.append(v)

    def query_bisect(self, p: Vec) -> int:
        hull = self.hull

        # 使用二分搜尋找到最佳點
        left, right = 0, len(hull) - 2
        while left <= right:
            mid = (left + right) // 2
            curr = p.dot(hull[mid])
            nxxt = p.dot(hull[mid + 1])
            if curr >= nxxt:
                left = mid + 1
            else:
                right = mid - 1

        return p.dot(hull[left])

    def query_mono(self, p: Vec) -> int:
        hull = self.hull

        # 使用單調隊列維護
        while len(hull) >= 2 and p.dot(hull[0]) >= p.dot(hull[1]):
            hull.popleft()
        return p.dot(hull[0])


def solve():
    n, L = map(int, input().split())
    A = [int(input()) for _ in range(n)]

    s = list(accumulate(A, initial=0))

    f = [inf] * (n + 1)
    f[0] = 0

    cht = ConvexHull()
    for i in range(1, n + 1):
        j = i - 1
        b_j = j + s[j] + L + 1
        vj = Vec(b_j, f[j] + b_j * b_j)
        cht.add(vj)

        a_i = i + s[i]
        p = Vec(-2 * a_i, 1)

        best = cht.query_bisect(p)
        # best = cht.query_mono(p)
        f[i] = best + a_i * a_i

    print(f[n])


if __name__ == "__main__":
    solve()
