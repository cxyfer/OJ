#
# @lc app=leetcode id=2787 lang=python3
#
# [2787] Ways to Express an Integer as Sum of Powers
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
MOD = int(1e9 + 7)
MAX_N, MAX_X = 300, 5
f = [[1] + [0] * MAX_N for _ in range(MAX_X + 1)]
for x in range(1, MAX_X + 1):
    for i in range(1, MAX_N + 1):
        v = i ** x
        if v > MAX_N:
            break
        for s in range(MAX_N, v - 1, -1):
            f[x][s] = (f[x][s] + f[x][s - v]) % MOD

class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        return f[x][n]
# @lc code=end

