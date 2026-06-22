"""
若選擇切割點 (i, j)，所有滿足 u > i 且 v < j 的弦 (u, v) 都會被消除。
反過來看，若要消除弦 (u, v)，切割點必須滿足 i < u 且 j > v。

因此，消除弦 (u, v) 時，所有滿足 u' >= u 且 v' <= v 的弦 (u', v') 也會被同時消除。
稱這些能被其他弦順帶消除的弦為「被支配」的弦。

對於相同上方端點 u 的所有弦，只需要保留最大的 max_v[u]。
接著按 u 遞增掃描，只保留下方端點能刷新前綴最大值的弦。
最後得到一組保留弦 (u_1, v_1), (u_2, v_2), ..., (u_k, v_k)，滿足
u_1 < u_2 < ... < u_k 且 v_1 < v_2 < ... < v_k。

刪除第 l 到第 r 條保留弦時，需要選擇 i < u_l 且 j > v_r，
所以 cost(l, r) = min_{i < u_l, j > v_r} A[i] * B[j]。
預處理 C[l] = min_{1 <= x < u_l} A[x]，D[r] = min_{v_r < x <= n} B[x]，
則 cost(l, r) = C[l] * D[r]。

令 f[i] 表示刪掉前 i 條保留弦的最小成本，則
f[i] = min_{0 <= j < i} f[j] + cost(j + 1, i)
    = min_{0 <= j < i} f[j] + C[j + 1] * D[i]

把每個決策 j 看成候選點 v_j = (C[j + 1], f[j])，目前右端點 i 看成查詢向量 p_i = (D[i], 1)，
則要查詢 min(p_i · v_j)。

由於 C[j + 1] 單調不增，為了用 Andrew 式維護下凸包，對第一維同時取反：
v_j = (-C[j + 1], f[j])，p_i = (-D[i], 1)。
內積不變，仍是 C[j + 1] * D[i] + f[j]。

可以用 query_bisect() 在下凸包上二分查詢；又因為 p_i 的 x 值單調不增，
最佳點索引單調往前移動，也可以用 query_mono() 做單調隊列查詢。
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


def solve() -> None:
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # 排序去重： O(m log m)
    # chords = [tuple(map(int, input().split())) for _ in range(m)]
    # chords.sort(key=lambda x: (x[0], -x[1]))
    # records = []
    # curr_v = 0
    # for u, v in chords:
    #     if v > curr_v:
    #         curr_v = v
    #         records.append((u, curr_v))

    # 基於值域的去重： O(n + m)
    max_v = [0] * (n + 1)
    for _ in range(m):
        u, v = map(int, input().split())
        max_v[u] = max(max_v[u], v)

    records = []
    curr_v = 0
    for u in range(1, n + 1):
        if max_v[u] > curr_v:
            curr_v = max_v[u]
            records.append((u, curr_v))

    k = len(records)

    pre_min = list(accumulate(A, func=min, initial=inf))
    suf_min = list(accumulate(B[::-1], func=min))[::-1]

    C = [0] * (k + 1)
    D = [0] * (k + 1)
    for idx, (u, v) in enumerate(records, start=1):
        C[idx] = pre_min[u - 1]
        D[idx] = suf_min[v]

    f = [0] * (k + 1)
    cht = ConvexHull()
    for i in range(1, k + 1):
        j = i - 1
        vj = Vec(-C[j + 1], f[j])  # 取反確保候選點 x 遞增
        cht.add(vj)

        p = Vec(-D[i], 1)
        # f[i] = cht.query_bisect(p)
        f[i] = cht.query_mono(p)

    print(f[k])


if __name__ == "__main__":
    solve()