#
# @lc app=leetcode id=3519 lang=python3
#
# [3519] Count Numbers with Non-Decreasing Digits 
#


# @lcpr-template-start
from preImport import *

# @lcpr-template-end
# @lc code=start
MOD = int(1e9) + 7


class Solution:
    def countNumbers(self, l: str, r: str, b: int) -> int:
        def convert(s: str) -> list[int]:
            # t = np.base_repr(int(s), base=b)
            # return list(map(int, t))
            x = int(s)
            digits = []
            while x:
                x, r = divmod(x, b)
                digits.append(r)
            digits.reverse()
            return digits

        high = convert(r)
        n = len(high)
        low = convert(l)
        diff = n - len(low)
        low = [0] * diff + low  # 補前導零，使 low 和 high 對齊

        @cache
        def dfs(i: int, pre: int, limit_low: bool, limit_high: bool) -> int:
            if i == n:
                return 1

            # 第 i 個數位可以從 lo 枚舉到 hi
            # 如果對數位還有其它約束，應該只在下面的 for 迴圈做限制，不應修改 lo 或 hi
            lo = low[i] if limit_low else 0
            hi = high[i] if limit_high else b - 1
            res = 0
            for d in range(max(lo, pre), hi + 1):
                res = (res + dfs(i + 1, d, limit_low and d == lo, limit_high and d == hi)) % MOD
            return res

        ans = dfs(0, 0, True, True)
        dfs.cache_clear()
        return ans
# @lc code=end

