#
# @lc app=leetcode id=2786 lang=python3
# @lcpr version=30203
#
# [2786] Visit Array Positions to Maximize Score
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
"""
    dp[i][0/1] 表示考慮前 i+1 個數字，且最後一個數字是奇數/偶數的情況下的最大值
"""
class Solution:
    def maxScore(self, nums: List[int], x: int) -> int:
        return self.solve1(nums, x)
        # return self.solve2(nums, x)

    def solve1(self, nums: List[int], x: int) -> int:
        n = len(nums)
        ans = nums[0]
        dp = [[float('-inf'), float('-inf')] for _ in range(n)]
        dp[0][nums[0] % 2] = nums[0]
        for i in range(1, n):
            p = nums[i] % 2 # parity, 0: even, 1: odd
            dp[i][p] = max(dp[i - 1][p] + nums[i], dp[i - 1][1 - p] + nums[i] - x)
            dp[i][1 - p] = dp[i - 1][1 - p]
            ans = max(ans, dp[i][p])
        return ans
    
    def solve2(self, nums: List[int], x: int) -> int:
        n = len(nums)
        ans = nums[0]
        f = [float('-inf'), float('-inf')]
        f[nums[0] % 2] = nums[0]
        for i in range(1, n):
            p = nums[i] % 2 # parity, 0: even, 1: odd
            f[p] = max(f[p] + nums[i], f[1 - p] + nums[i] - x)
            ans = max(ans, f[p])
        return ans
# @lc code=end

sol = Solution()
print(sol.maxScore([2,3,6,1,9,2], 5)) # 13
print(sol.maxScore([2,4,6,8], 3)) # 20
print(sol.maxScore([8,50,65,85,8,73,55,50,29,95,5,68,52,79], 74)) # 470


#
# @lcpr case=start
# [2,3,6,1,9,2]\n5\n
# @lcpr case=end

# @lcpr case=start
# [2,4,6,8]\n3\n
# @lcpr case=end

#

