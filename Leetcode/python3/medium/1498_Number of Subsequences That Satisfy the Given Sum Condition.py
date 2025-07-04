#
# @lc app=leetcode id=1498 lang=python3
#
# [1498] Number of Subsequences That Satisfy the Given Sum Condition
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
MOD = 10 ** 9 + 7
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        n = len(nums)
        ans = 0
        nums.sort()
        i, j = 0, n - 1
        while i <= j:
            if nums[i] + nums[j] <= target:
                ans += pow(2, j - i, MOD)
                ans %= MOD
                i += 1
            else:
                j -= 1
        return ans
# @lc code=end

