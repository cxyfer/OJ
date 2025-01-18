#
# @lc app=leetcode id=2320 lang=python3
# @lcpr version=30201
#
# [2320] Count Number of Ways to Place Houses
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start

sys.setrecursionlimit(10000)

class Solution:
    """
        Dynamic Programming + 乘法原理
        Similar to 198. House Robber
        Similat to 70. Climbing Stairs
    """
    def countHousePlacements(self, n: int) -> int:
        # return self.solve1(n)
        return self.solve2(n)
    def solve1(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [0] * (max(2, n + 1))
        dp[0], dp[1] = 1, 2
        for i in range(2, n+1):
            dp[i] = (dp[i-1] + dp[i-2]) % MOD
        return dp[n] ** 2 % MOD
    def solve2(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        f0, f1 = 1, 2
        for i in range(2, n+1):
            f0, f1 = f1, (f0 + f1) % MOD
        return f1 ** 2 % MOD
# @lc code=end

sol = Solution()
print(sol.countHousePlacements(1000)) # 500478595

#
# @lcpr case=start
# 1\n
# @lcpr case=end

# @lcpr case=start
# 2\n
# @lcpr case=end

#

