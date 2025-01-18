#
# @lc app=leetcode.cn id=1137 lang=python3
#
# [1137] 第 N 个泰波那契数
#
from preImport import *
# @lc code=start
class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0 for _ in range(max(3,n+1))]
        dp[0], dp[1], dp[2] = 0, 1, 1
        for i in range(3,n+1):
            dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
        return dp[n]
# @lc code=end

