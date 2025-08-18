#
# @lc app=leetcode id=2348 lang=python3
#
# [2348] Number of Zero-Filled Subarrays
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        # return sum((n := len(list(g))) * (n + 1) // 2 for k, g in groupby(nums) if k == 0)
        ans = 0
        for k, g in groupby(nums):
            if k != 0:
                continue
            n = len(list(g))
            ans += n * (n + 1) // 2
        return ans
# @lc code=end

sol = Solution()
print(sol.zeroFilledSubarray([1,3,0,0,2,0,0,4]))