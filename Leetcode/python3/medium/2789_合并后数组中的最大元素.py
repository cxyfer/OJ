#
# @lc app=leetcode.cn id=2789 lang=python3
#
# [2789] 合并后数组中的最大元素
#
from preImport import *
# @lc code=start
class Solution:
    """
        Greedy，由後往前合併
    """
    def maxArrayValue(self, nums: List[int]) -> int:
        n = len(nums)
        s = nums[n-1]
        for i in range(n-2, -1, -1):
            if nums[i] <= s: # 可以合併
                s += nums[i]
            else:
                s = nums[i]
        return s
# @lc code=end

