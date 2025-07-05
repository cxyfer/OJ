#
# @lc app=leetcode id=1397 lang=python3
#
# [1397] Find All Good Strings
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
MOD = int(1e9 + 7)
class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        m = len(evil)
        pi = [0] * m
        ln = 0
        for i in range(1, m):
            while ln and evil[i] != evil[ln]:
                ln = pi[ln - 1]
            if evil[i] == evil[ln]:
                ln += 1
            pi[i] = ln

        high = list(map(ord, s2))
        low = list(map(ord, s1))
        @cache
        def dfs(i: int, j: int, limit_low: bool, limit_high: bool) -> int:
            if i == n:
                return 1 if j < m else 0

            # 第 i 個數位可以從 lo 枚舉到 hi
            # 如果對數位還有其它約束，應該只在下面的 for 迴圈做限制，不應修改 lo 或 hi
            lo = low[i] if limit_low else ord('a')
            hi = high[i] if limit_high else ord('z')

            res = 0
            for d in range(lo, hi + 1):
                ln = j
                while ln and chr(d) != evil[ln]:
                    ln = pi[ln - 1]
                if chr(d) == evil[ln]:
                    ln += 1
                if ln == m:
                    continue
                res += dfs(i + 1, ln, limit_low and d == lo, limit_high and d == hi)
            return res % MOD

        return dfs(0, 0, True, True)
# @lc code=end

sol = Solution()
print(sol.findGoodStrings(2, "aa", "da", "b"))