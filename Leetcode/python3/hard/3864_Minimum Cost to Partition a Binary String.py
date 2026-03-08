#
# @lc app=leetcode id=3864 lang=python3
#
# [3864] Minimum Cost to Partition a Binary String
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def minCost(self, s: str, encCost: int, flatCost: int) -> int:
        n = len(s)
        pre = list(accumulate(map(int, s), initial=0))

        def dfs(l: int, r: int) -> int:
            ln = r - l + 1
            x = pre[r + 1] - pre[l]
            res = (ln * x * encCost) if x > 0 else flatCost
            if ln & 1 == 0:
                mid = (l + r) // 2
                res = min(res, dfs(l, mid) + dfs(mid + 1, r))
            return res

        return dfs(0, n - 1)
# @lc code=end

