#
# @lc app=leetcode id=312 lang=python3
# @lcpr version=30203
#
# [312] Burst Balloons
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
    Matrix Chain Multiplication
    前後補1，取最小改成取最大
"""
# @lc code=start
class Solution1:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        nums = [1] + nums + [1]  # add 1 to both ends

        @cache
        def dfs(left: int, right: int) -> int:
            if right - left <= 1:
                return 0
            res = 0
            for i in range(left + 1, right):
                cur = nums[left] * nums[i] * nums[right]
                cur += dfs(left, i) + dfs(i, right)
                res = max(res, cur)
            return res

        return dfs(0, n + 1)
    
class Solution2:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        nums = [1] + nums + [1]
        dp = [[0] * (n + 2) for _ in range(n + 2)]
        for ln in range(3, n + 3):  # length of subarray
            for l in range(n + 3 - ln):
                r = l + ln - 1
                for m in range(l + 1, r):
                    dp[l][r] = max(
                        dp[l][r],
                        dp[l][m] + dp[m][r] + nums[l] * nums[m] * nums[r])
        return dp[0][n + 1]
    
class Solution3:
    def maxCoins(self, nums: List[int]) -> int:
        p = [1] + nums + [1]
        n = len(p) - 1

        # dp[i][j] 表示從第 M_i 到 M_j 的最小乘法次數
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        # 初始化
        for i in range(n + 1):
            dp[i][i] = 0

        for ln in range(2, n + 1): # 枚舉長度
            for i in range(1, n + 1 - (ln - 1)): # 枚舉起點
                j = i + ln - 1 # 終點
                for k in range(i, j):
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k + 1][j] + p[i - 1] * p[k] * p[j])
                    
        return dp[1][n]

# class Solution(Solution1):
# class Solution(Solution2):  
class Solution(Solution3):
    pass
# @lc code=end

sol = Solution()
print(sol.maxCoins([3,1,5,8]))



#
# @lcpr case=start
# [3,1,5,8]\n
# @lcpr case=end

# @lcpr case=start
# [1,5]\n
# @lcpr case=end

#
