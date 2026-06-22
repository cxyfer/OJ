"""
題意說了，當選擇切 (i, j) 時，所有 u > i, v < j 的弦 (u, v) 都會被消除，
反過來說就是想要消除弦 (u, v) 時，需要選擇 i < u, j > v。

當消除弦 (u, v) 時，只要其他弦 (u', v') 滿足 u' >= u, v' <= v 就會被同時消除，
為方便說明，以下稱能在消除其他弦時被順帶消除的弦是「被支配」的。
用圖形來理解就是交叉的兩條線，其中右上左下的這條會被另外一條支配。

注意到對於 u 相同的若干組弦，消除最大的 (u, max_v[u]) 就會同時消除其他 (u, v) (v < max_v[u])，
且僅考慮相同 u 時，最大的 v 也是無法被支配的，因此我們只需要保留每個 u 對應的最大 v 即可。

這樣對 u 排序後可以自然得到 u1 < u2，此時若發現 v2 <= v1，則 (u2, v2) 就會被 (u1, v1) 支配，因此也可以刪除 (u2, v2)。
最後會得到一組沒有交叉的弦 (u1, v1), (u2, v2), ..., (uk, vk)，其中 u1 < u2 < ... < uk 且 v1 < v2 < ... < vk。

那麼如果要刪除 [l, r] 的弦，則需要選擇 i < ul, j > vr，此時 cost(l, r) = min_{i < ul, j > vr} A[i] * B[j]。
這裡可以分別用前綴和後綴最小值來遇處理，定義 C[i] = min_{1 <= x < i} A[x]，D[i] = min_{i < x <= n} B[x]，
則 cost(l, r) = C[ul] * D[vr]。

令 f[i] 是消除前 i 條弦的最小成本，
則轉移式為 f[i] = min_{j < i} f[j] + cost(j + 1, i)
               = min_{j < i} f[j] + C[u_j] * D[v_i]
這種兩項相乘的 DP 就可以使用 CHT 來優化，
令 p = (D[v_i], 1), vj = (C[u_j], f[j])，查詢 min(p·vj)。

但有個問題是 C[u_j] 是遞減的，為了能夠使用 Andrew 求下凸包，可以對 x 取負，令 p = (-D[v_i], 1)，vj = (-C[u_j], f[j])
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
    chords = [tuple(map(int, input().split())) for _ in range(m)]
    chords.sort(key=lambda x: (x[0], -x[1]))
    records = []
    curr_v = 0
    for u, v in chords:
        if v > curr_v:
            curr_v = v
            records.append((u, curr_v))

    # 基於值域的去重： O(n + m)
    # max_v = [0] * (n + 1)
    # for _ in range(m):
    #     u, v = map(int, input().split())
    #     max_v[u] = max(max_v[u], v)

    # records = []
    # curr_v = 0
    # for u in range(1, n + 1):
    #     if max_v[u] > curr_v:
    #         curr_v = max_v[u]
    #         records.append((u, curr_v))

    k = len(records)

    if k == 0:
        print(0)
        return

    pre_min = list(accumulate(A, func=min, initial=inf))
    suf_min = list(accumulate(B[::-1], func=min))[::-1]

    C = [0] * (k + 1)
    D = [0] * (k + 1)
    for idx, (u, v) in enumerate(records, start=1):
        C[idx] = pre_min[u - 1]
        D[idx] = suf_min[v]

    f = [0] * (k + 1)
    cht = ConvexHull()
    for r in range(1, k + 1):
        v = Vec(-C[r], f[r - 1])
        cht.add(v)

        p = Vec(-D[r], 1)
        # f[r] = cht.query_bisect(p)
        f[r] = cht.query_mono(p)

    print(f[k])


if __name__ == "__main__":
    solve()
