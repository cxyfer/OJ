#
# @lc app=leetcode id=3826 lang=python3
#
# [3826] Minimum Partition Score
#


# @lcpr-template-start
from re import S

from preImport import *


# @lcpr-template-end
# @lc code=start
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
    - 若查詢不具單調性，請使用 ConvexHull 的二分 query()。
    """

    def __init__(self):
        self.hull = deque()  # min 維護下凸包

    def _bad(self, a: Vec, b: Vec, c: Vec) -> bool:
        # 順時針方向或共線，此時 b 點不會是「下凸包」的一部分
        return (b - a).det(c - b) <= 0

    def add(self, v: Vec) -> None:
        hull = self.hull

        # 如果新點與最後一個點 x 相同，只保留對應 mode 下較優的 y
        if hull and hull[-1].x == v.x:
            if hull[-1].y <= v.y:
                return
            hull.pop()

        # 維護凸包性質，移除不可能成為凸包的中間點
        while len(hull) >= 2 and self._bad(hull[-2], hull[-1], v):
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


class Solution1:
    def minPartitionScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pre = list(accumulate(nums, initial=0))

        f = [inf] * (n + 1)
        f[0] = 0

        for K in range(1, k + 1):
            nf = [inf] * (n + 1)
            cht = ConvexHull()

            s = pre[K - 1]
            cht.add(Vec(s, f[K - 1] + s * s - s))

            max_i = n - (k - K)
            for i in range(K, max_i + 1):
                s = pre[i]
                p = Vec(-2 * s, 1)

                # best = cht.query_bisect(p)
                best = cht.query_mono(p)
                nf[i] = best + s * s + s

                if f[i] < inf:
                    cht.add(Vec(s, f[i] + s * s - s))
            f = nf

        return f[n] // 2


class Solution3:
    def minPartitionScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        s = list(accumulate(nums, initial=0))

        def cost(l: int, r: int) -> int:  # cost of [l, r)
            v = s[r] - s[l]
            return v * (v + 1) // 2

        f = [float("inf")] * (n + 1)
        nf = [float("inf")] * (n + 1)
        f[0] = 0

        def solve(l: int, r: int, opt_l: int, opt_r: int):
            if l > r:
                return
            mid = (l + r) // 2

            best_val = float("inf")
            opt = -1  # opt[mid]
            for p in range(opt_l, min(opt_r, mid - 1) + 1):
                val = f[p] + cost(p, mid)
                if val < best_val:
                    best_val = val
                    opt = p
            nf[mid] = best_val

            solve(l, mid - 1, opt_l, opt)  # 左側的決策點一定 <= opt[mid]
            solve(mid + 1, r, opt, opt_r)  # 右側的決策點一定 >= opt[mid]

        for j in range(1, k + 1):
            solve(j, n, j - 1, n - 1)  # 在 D&C 的過程中計算 nf
            f = nf.copy()
        return f[n]


Solution = Solution1
# Solution = Solution3
# @lc code=end

sol = Solution()
print(sol.minPartitionScore([5, 1, 2, 1], 2))  # 25
print(sol.minPartitionScore([1, 2, 3, 4], 1))  # 55
print(sol.minPartitionScore([1, 1, 1], 3))  # 3
print(sol.minPartitionScore([13, 8, 19], 2))  # 421
