#
# @lc app=leetcode id=494 lang=python3
# @lcpr version=30204
#
# [494] Target Sum
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
""" Dynamic Programming
    - pos - neg = sum(nums)
    - pos + neg = target
    => pos = (sum(nums) + target) // 2
    dp[i][j] 為考慮前 i 個數字，和為 j 的方法數
"""
class Solution1a:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        pos = target + sum(nums)
        if pos % 2 or pos < 0:
            return 0
        pos //= 2
        @cache
        def dfs(i: int, j: int) -> int:
            if i == 0:
                return 1 if j == 0 else 0
            if j < nums[i - 1]: # Pruining
                return dfs(i - 1, j)
            return dfs(i - 1, j) + dfs(i - 1, j - nums[i - 1])
        return dfs(n, pos)
    
class Solution1b:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        pos = sum(nums) + target
        if pos & 1 or pos < 0:
            return 0
        k = pos // 2
        f = [0] * (k + 1)
        f[0] = 1
        for x in nums:
            for j in range(k, x - 1, -1):
                f[j] += f[j - x]
        return f[k]

# class Solution(Solution1a):
class Solution(Solution1b):
    pass
# @lc code=end

sol = Solution()
print(sol.findTargetSumWays([1,1,1,1,1], 3)) # 5
print(sol.findTargetSumWays([1], 1)) # 1 
print(sol.findTargetSumWays([1], 2)) # 0
print(sol.findTargetSumWays([0,0,0,0,0,0,0,0,1], 1)) # 256

#
# @lcpr case=start
# [1,1,1,1,1]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1]\n1\n
# @lcpr case=end

#

