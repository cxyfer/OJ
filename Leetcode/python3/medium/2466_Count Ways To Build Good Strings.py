#
# @lc app=leetcode id=2466 lang=python3
# @lcpr version=30201
#
# [2466] Count Ways To Build Good Strings
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    """
        DP
        Similar to 70. Climbing Stairs
    """
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [0] * (high + 1)
        dp[0] = 1
        for i in range(1, high + 1):
            if i >= zero: dp[i] += dp[i-zero]
            if i >= one: dp[i] += dp[i-one]
            dp[i] %= MOD
        return sum(dp[low:high+1]) % MOD
# @lc code=end



#
# @lcpr case=start
# 3\n3\n1\n1\n
# @lcpr case=end

# @lcpr case=start
# 2\n3\n1\n2\n
# @lcpr case=end

#

