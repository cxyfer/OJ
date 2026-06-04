#
# @lc app=leetcode id=3753 lang=python3
#
# [3753] Total Waviness of Numbers in Range II
#


# @lcpr-template-start
from numpy import c_

from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1a:
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


class Solution1b:
    def totalWaviness(self, l: int, r: int) -> int:
        n = len(str(r))
        diff = len(str(r)) - len(str(l))
        high = list(map(int, str(r)))
        low = list(map(int, str(l).zfill(n)))

        @cache
        def dfs(i: int, pre1: int, pre2: int, limit_low: bool, limit_high: bool) -> tuple[int, int]:
            if i == n:
                return (1, 0)  # (total child, total waviness)

            lo = low[i] if limit_low else 0
            hi = high[i] if limit_high else 9

            tot = res = 0
            if i < diff and limit_low:
                tot, res = dfs(i + 1, -1, -1, True, False)
            for d in range(1 if i < diff and limit_low else lo, hi + 1):
                is_waviness = pre1 != -1 and pre2 != -1 and ((pre1 < pre2 > d) or (pre1 > pre2 < d))
                c_tot, c_res = dfs(i + 1, pre2, d, limit_low and d == lo, limit_high and d == hi)
                tot += c_tot
                res += c_res + c_tot * int(is_waviness)
            return (tot, res)

        return dfs(0, -1, -1, True, True)[1]


# Solution = Solution1a
Solution = Solution1b
# @lc code=end

