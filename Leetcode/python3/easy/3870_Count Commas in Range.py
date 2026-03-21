#
# @lc app=leetcode id=3870 lang=python3
#
# [3870] Count Commas in Range
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def countCommas(self, n: int) -> int:
        k = (len(str(n)) - 1) // 3
        # return k * (n + 1) - 1000 * (10 ** (3 * k) - 1) // 999
        ans = 0
        for d in range(1, k + 1):
            ans += n - 10 ** (3 * d) + 1
        return ans
# @lc code=end

