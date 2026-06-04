#
# @lc app=leetcode id=3751 lang=python3
#
# [3751] Total Waviness of Numbers in Range I
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def totalWaviness(self, l: int, r: int) -> int:
        n = len(str(r))
        diff = len(str(r)) - len(str(l))
        high = list(map(int, str(r)))
        low = list(map(int, str(l).zfill(n)))

        @cache
        def dfs(i: int, pre1: int, pre2: int, cnt: int, limit_low: bool, limit_high: bool) -> int:
            if i == n:
                return cnt

            lo = low[i] if limit_low else 0
            hi = high[i] if limit_high else 9

            res = 0
            if i < diff and limit_low:
                res += dfs(i + 1, -1, -1, 0, True, False)
            for d in range(1 if i < diff and limit_low else lo, hi + 1):
                is_waviness = pre1 != -1 and pre2 != -1 and ((pre1 < pre2 > d) or (pre1 > pre2 < d))
                res += dfs(i + 1, pre2, d, cnt + int(is_waviness), limit_low and d == lo, limit_high and d == hi)
            return res

        return dfs(0, -1, -1, 0, True, True)
# @lc code=end
sol = Solution()
print(sol.totalWaviness(120, 130))  # 3