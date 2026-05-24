#
# @lc app=leetcode id=3936 lang=python3
#
# [3936] Minimum Swaps to Move Zeros to End
#

# @lcpr-template-start
from preImport import *
# @lcpr-template-end

# @lc code=start
class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        n = len(nums)
        cnt0 = nums.count(0)
        return sum(nums[i] != 0 for i in range(n - cnt0, n))
# @lc code=end

