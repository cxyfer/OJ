#
# @lc app=leetcode id=3512 lang=python3
#
# [3512] Minimum Operations to Make Array Sum Divisible by K
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return sum(nums) % k
# @lc code=end

