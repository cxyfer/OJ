from typing import List
from itertools import accumulate
from math import inf

"""
斜率優化DP (Convex Hull Trick, CHT)

以內積來維護凸包，查詢 min p·v 或 max p·v，以下以 min p·v 為例說明。
假設有一個 DP 狀態轉移方程式為 f[i] = min_{j < i} (f[j] + S[i] * S[j])，直接轉移需要枚舉 O(n) 個 j 。
但可以把相乘的 S[i] * S[j] 視作內積相乘，即將原式用內積表示成 (S[i], 1) · (S[j], f[j])，
令 p = (S[i], 1)，vj = (S[j], f[j])，則可以使用 CHT 來維護 vj，查詢 min(p·vj)。

根據內積的幾何性質（||p|| * ||vj|| * cos(theta)，其中 theta 是 p 與 vj 的夾角），
而 ||vj|| * cos(theta) 就是 vj 在 p 上的投影（即從原點到 vj 的向量在 p 方向上的投影），
因此所求的 vj 必定在下凸包上，且 vj 的投影長度會隨著 x 值的增加而先減後增。
"""

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
    mode='min'：維護下凸包，查詢 min p·v
    mode='max'：維護上凸包，查詢 max p·v

    注意：
    - add() 的點需要依 x 遞增加入。
    - query() 不要求查詢向量單調，使用二分搜尋。
    """

    def __init__(self, mode: str = "min"):
        assert mode in ("min", "max")
        self.mode = mode
        self.hull = []

    def _bad(self, a: Vec, b: Vec, c: Vec) -> bool:
        cross = (b - a).det(c - b)

        if self.mode == "min":
            # 順時針方向或共線，此時 b 點不會是「下凸包」的一部分
            return cross <= 0 
        else:
            # 逆時針方向或共線，此時 b 點不會是「上凸包」的一部分
            return cross >= 0

    def add(self, v: Vec) -> None:
        hull = self.hull

        if hull and hull[-1].x == v.x:
            if self.mode == "min":
                if hull[-1].y <= v.y:
                    return
            else:
                if hull[-1].y >= v.y:
                    return
            hull.pop()

        while len(hull) >= 2 and self._bad(hull[-2], hull[-1], v):
            hull.pop()

        hull.append(v)

    def query(self, p: Vec) -> int:
        hull = self.hull

        left, right = 0, len(hull) - 2
        while left <= right:
            mid = (left + right) // 2
            curr = p.dot(hull[mid])
            nxxt = p.dot(hull[mid + 1])
            if self.mode == "min":
                if curr >= nxxt:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if curr <= nxxt:
                    left = mid + 1
                else:
                    right = mid - 1

        return p.dot(hull[left])


class Solution3826:
    def minPartitionScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pre = list(accumulate(nums, initial=0))

        f = [inf] * (n + 1)
        f[0] = 0

        for K in range(1, k + 1):
            nf = [inf] * (n + 1)
            cht = ConvexHull(mode="min")

            s = pre[K - 1]
            cht.add(Vec(s, f[K - 1] + s * s - s))

            max_i = n - (k - K)
            for i in range(K, max_i + 1):
                s = pre[i]
                p = Vec(-2 * s, 1)

                best = cht.query(p)
                nf[i] = best + s * s + s

                if f[i] < inf:
                    cht.add(Vec(s, f[i] + s * s - s))

            f = nf

        return f[n] // 2
