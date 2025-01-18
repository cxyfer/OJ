#
# @lc app=leetcode id=213 lang=python3
# @lcpr version=30201
#
# [213] House Robber II
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    """
        Similar to 198. House Robber
    """
    def rob(self, nums: List[int]) -> int:
        # return self.solve1(nums)
        # return self.solve2(nums)
        return self.solve3(nums)
    def solve1(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        @cache
        def dfs(i: int, lo: int):
            if i < lo:
                return 0
            return max(dfs(i-1, lo), dfs(i-2, lo) + nums[i]) # rob or not rob
        return max(dfs(n-2, 0), dfs(n-1, 1)) # rob house_0 / not rob house_0
    def solve2(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        def f(lo: int, hi: int) -> int: #[lo, hi)
            m = (hi - lo)
            dp = [0] * (m + 1)
            dp[1] = nums[lo]
            for i in range(2, m + 1):
                dp[i] = max(dp[i-1], dp[i-2] + nums[lo + i - 1])
            return dp[m]
        return max(f(0, n-1), f(1, n))
    def solve3(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        def f(lo: int, hi: int) -> int: # [lo, hi)
            f0, f1 = 0, 0
            for i in range(lo, hi):
                f0, f1 = f1, max(f1, f0 + nums[i])
            return f1
        return max(f(0, n-1), f(1, n))
# @lc code=end
sol = Solution()
print(sol.rob([2,3,2])) # 3
print(sol.rob([1,2,3,1])) # 4
print(sol.rob([1,2,3])) # 3
print(sol.rob([1])) # 1
#
# @lcpr case=start
# [2,3,2]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

#

