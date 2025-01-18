#
# @lc app=leetcode id=198 lang=python3
# @lcpr version=30201
#
# [198] House Robber
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        # return self.solve1(nums)
        # return self.solve2(nums)
        return self.solve3(nums)
    def solve1(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def dfs(i: int) -> int:
            if i < 0: return 0
            return max(dfs(i-1), dfs(i-2) + nums[i]) # not rob / rob
        return dfs(n-1)
    def solve2(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n + 1)
        dp[1] = nums[0]
        for i in range(2, n + 1):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i-1]) # not rob / rob
        return dp[n]
    def solve3(self, nums: List[int]) -> int:
        f0 = f1 = 0
        for x in nums:
            f0, f1 = f1, max(f1, f0 + x) # not rob / rob
        return f1
# @lc code=end



#
# @lcpr case=start
# [1,2,3,1]\n
# @lcpr case=end

# @lcpr case=start
# [2,7,9,3,1]\n
# @lcpr case=end

#

