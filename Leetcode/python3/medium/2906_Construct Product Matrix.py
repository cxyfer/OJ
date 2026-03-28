#
# @lc app=leetcode id=2906 lang=python3
#
# [2906] Construct Product Matrix
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
MOD = 12345

class Solution1:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ans = [[0] * n for _ in range(m)]
        pre = 1
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                ans[i][j] = pre
                pre = pre * x % MOD
        suf = 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                ans[i][j] = ans[i][j] * suf % MOD
                suf = suf * grid[i][j] % MOD
        return ans

MOD = 12345
FACTORS = (3, 5, 823)

class ModValue:
    __slots__ = ("exps", "rem")

    def __init__(self, val: int = 1):
        self.exps = [0] * len(FACTORS)
        v = val
        for i, p in enumerate(FACTORS):
            while v % p == 0:
                self.exps[i] += 1
                v //= p
        self.rem = v % MOD

    @classmethod
    def from_parts(cls, exps, rem):
        obj = cls.__new__(cls)
        obj.exps = exps
        obj.rem = rem % MOD
        return obj

    def to_val(self) -> int:
        res = self.rem
        for p, e in zip(FACTORS, self.exps):
            res = (res * pow(p, e, MOD)) % MOD
        return res

    def __mul__(self, other: "ModValue") -> "ModValue":
        return ModValue.from_parts(
            [a + b for a, b in zip(self.exps, other.exps)],
            self.rem * other.rem % MOD,
        )

    def __truediv__(self, other: "ModValue") -> "ModValue":
        return ModValue.from_parts(
            [a - b for a, b in zip(self.exps, other.exps)],
            self.rem * pow(other.rem, -1, MOD) % MOD,
        )

class Solution2:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])

        vals = [[ModValue(x) for x in row] for row in grid]

        tot = ModValue(1)
        for row in vals:
            for x in row:
                tot = tot * x

        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                ans[i][j] = (tot / vals[i][j]).to_val()
        return ans

FACTORS = (3, 5, 823)

class Solution3:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])

        exps = [0] * len(FACTORS)
        rem = 1
        for row in grid:
            for x in row:
                for i, p in enumerate(FACTORS):
                    while x % p == 0:
                        exps[i] += 1
                        x //= p
                rem = rem * x % MOD

        ans = [[0] * n for _ in range(m)]
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                cur = [0] * len(FACTORS)
                for k, p in enumerate(FACTORS):
                    while x % p == 0:
                        cur[k] += 1
                        x //= p
                res = 1
                for p, e1, e2 in zip(FACTORS, exps, cur):
                    res = res * pow(p, e1 - e2, MOD) % MOD
                res *= rem * pow(x, -1, MOD) % MOD
                ans[i][j] = res % MOD
        return ans

Solution = Solution1
# Solution = Solution2
# Solution = Solution3
# @lc code=end

