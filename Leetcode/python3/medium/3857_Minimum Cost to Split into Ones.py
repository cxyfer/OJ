#
# @lc app=leetcode id=3857 lang=python3
#
# [3857] Minimum Cost to Split into Ones
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def minCost(self, n: int) -> int:
        @cache
        def dfs(n: int) -> int:
            if n == 1:
                return 0
            res = float("inf")
            for x in range(1, n // 2 + 1):
                res = min(res, dfs(x) + dfs(n - x) + x * (n - x))
            return res

        return dfs(n)


class Solution2:
    def minCost(self, n: int) -> int:
        return n * (n - 1) // 2


# Solution = Solution1
Solution = Solution2
# @lc code=end

