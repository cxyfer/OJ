#
# @lc app=leetcode id=2999 lang=python3
#
# [2999] Count the Number of Powerful Integers
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        high = list(map(int, str(finish)))
        n = len(high)
        low = list(map(int, str(start).zfill(n)))  # 補前導零，使 low 和 high 對齊
        s = list(map(int, s))

        @cache
        def dfs(i: int, limit_low: bool, limit_high: bool) -> int:
            if i == n:
                return 1

            # 第 i 個數位可以從 lo 枚舉到 hi
            # 如果對數位還有其它約束，應該只在下面的 for 迴圈做限制，不應修改 lo 或 hi
            lo = low[i] if limit_low else 0
            hi = high[i] if limit_high else 9

            if i >= n - len(s):  # 只能填 s 的數字
                d = s[i - (n - len(s))]
                ranges = [d] if lo <= d <= min(hi, limit) else []
            else:
                ranges = range(lo, min(hi, limit) + 1)

            res = 0
            for d in ranges:
                res += dfs(i + 1, limit_low and d == lo, limit_high and d == hi)
            return res

        return dfs(0, True, True)
# @lc code=end

