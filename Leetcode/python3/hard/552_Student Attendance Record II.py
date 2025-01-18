#
# @lc app=leetcode id=552 lang=python3
# @lcpr version=30202
#
# [552] Student Attendance Record II
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7
        # 用 @cache 裝飾器會超時
        memo = [[[-1] * 3 for _ in range(2)] for _ in range(n)]
        def dfs(i: int, a: int, l: int) -> int:
            if i == n:
                return 1
            if memo[i][a][l] != -1:
                return memo[i][a][l]
            ans = 0
            if a < 1: # 可以再缺席一天
                ans += dfs(i + 1, a + 1, 0)
            if l < 2: # 可以再遲到一天
                ans += dfs(i + 1, a, l + 1)
            ans += dfs(i + 1, a, 0)
            ans %= MOD
            memo[i][a][l] = ans
            return ans
        return dfs(0, 0, 0)
# @lc code=end



#
# @lcpr case=start
# 2\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

# @lcpr case=start
# 10101\n
# @lcpr case=end

#

