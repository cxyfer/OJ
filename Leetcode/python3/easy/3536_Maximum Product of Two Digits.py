#
# @lc app=leetcode id=3536 lang=python3
#
# [3536] Maximum Product of Two Digits
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maxProduct(self, n: int) -> int:
        digits = map(int, str(n))
        ans = mx = 0
        for d in digits:
            ans = max(ans, mx * d)
            mx = max(mx, d)
        return ans
# @lc code=end

