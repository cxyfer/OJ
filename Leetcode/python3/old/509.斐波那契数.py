#
# @lc app=leetcode.cn id=509 lang=python3
#
# [509] 斐波那契数
#

# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        DP = [0 for _ in range(n+1)]
        DP[0] = 0
        DP[1] = 1
        for i in range(2, n+1):
            DP[i] = DP[i-1] + DP[i-2]
        return DP[n]

# @lc code=end

