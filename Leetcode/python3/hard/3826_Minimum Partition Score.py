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
    mode='min'：維護下凸包，查詢 min p·v
    mode='max'：維護上凸包，查詢 max p·v

    注意：
    - add() 的點需要依 x 遞增加入。
    - query() 不要求查詢向量單調，使用二分搜尋。
    """

    def __init__(self, mode: str = "min"):
        assert mode in ("min", "max")
        self.mode = mode
        self.hull = []  # min 維護下凸包，max 維護上凸包

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

        # 如果新點與最後一個點的 x 坐標相同，則保留 y 坐標更小（min）或更大（max）的點
        if hull and hull[-1].x == v.x:
            if self.mode == "min":
                if hull[-1].y <= v.y:
                    return
            else:
                if hull[-1].y >= v.y:
                    return
            hull.pop()

        # 檢查最後兩個點與新點是否形成凸包，如果不是凸包，則移除最後一個點
        while len(hull) >= 2 and self._bad(hull[-2], hull[-1], v):
            hull.pop()

        hull.append(v)

    def query(self, p: Vec) -> int:
        hull = self.hull

        # 使用二分搜尋找到最佳點
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


class Solution1:
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

                nf[i] = cht.query(p) + s * s + s

                if f[i] < inf:
                    cht.add(Vec(s, f[i] + s * s - s))

            f = nf

        return f[n] // 2


class Solution2:
    def minPartitionScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pre = list(accumulate(nums, initial=0))

        f = [inf] * (n + 1)
        f[0] = 0

        for K in range(1, k + 1):
            nf = [inf] * (n + 1)
            q = deque()

            s = pre[K - 1]
            q.append(Vec(s, f[K - 1] + s * s - s))

            max_i = n - (k - K)
            for i in range(K, max_i + 1):
                s = pre[i]
                p = Vec(-2 * s, 1)

                # 因為查詢向量 (-2 * s, 1) 是只會往左旋轉的，因此最佳點只會往右移動，可以使用單調隊列維護
                while len(q) > 1 and p.dot(q[0]) >= p.dot(q[1]):
                    q.popleft()

                v = Vec(s, f[i] + s * s - s)
                nf[i] = p.dot(q[0]) + s * s + s

                while len(q) > 1 and (q[-1] - q[-2]).det(v - q[-1]) <= 0:
                    q.pop()

                q.append(v)

            f = nf

        return f[n] // 2


class Solution3:
    def minPartitionScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        s = list(accumulate(nums, initial=0))

        def cost(l: int, r: int) -> int:  # cost of [l, r)
            v = s[r] - s[l]
            return v * (v + 1) // 2

        f = [float('inf')] * (n + 1)
        nf = [float('inf')] * (n + 1)
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


# Solution = Solution1
# Solution = Solution2
Solution = Solution3
# @lc code=end

sol = Solution()
print(sol.minPartitionScore([5,1,2,1], 2))  # 25
print(sol.minPartitionScore([1,2,3,4], 1))  # 55
print(sol.minPartitionScore([1,1,1], 3))  # 3
print(sol.minPartitionScore([13,8,19], 2))  # 421