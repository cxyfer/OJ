#
# @lc app=leetcode id=3862 lang=python3
#
# [3862] Find the Smallest Balanced Index
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def smallestBalancedIndex(self, nums: list[int]) -> int:
        n = len(nums)
        pre, suf = sum(nums), 1
        for i in range(n - 1, -1, -1):
            x = nums[i]
            pre -= x
            if suf > pre:
                break
            if suf == pre:
                return i  # 因為答案是唯一的，所以可以提前返回
            suf *= x
        return -1
# @lc code=end

