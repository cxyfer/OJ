#
# @lc app=leetcode.cn id=1877 lang=python3
#
# [1877] 数组中最大数对和的最小值
#
from preImport import *
# @lc code=start
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        ans = 0
        for i in range(n // 2):
            ans = max(ans, nums[i] + nums[n - 1 - i])
        return ans
# @lc code=end

