#
# @lc app=leetcode id=279 lang=python3
# @lcpr version=30204
#
# [279] Perfect Squares
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
Dynamic Programming
dp[i] 表示和為i的完全平方數的最小個數
"""
# @lc code=start
N = int(1e4)
f = [inf] * (N + 1)
f[0] = 0
for i in range(1, isqrt(N) + 1):
    for j in range(i * i, N + 1):
        f[j] = min(f[j], f[j - i * i] + 1)


class Solution:
    def numSquares(self, n: int) -> int:
        return f[n]
# @lc code=end



#
# @lcpr case=start
# 12\n
# @lcpr case=end

# @lcpr case=start
# 13\n
# @lcpr case=end

#

