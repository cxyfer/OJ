#
# @lc app=leetcode.cn id=334 lang=python3
#
# [334] 递增的三元子序列
#
from en.Python3.mod.preImport import *
# @lc code=start
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        first, second = nums[0], float('inf')
        for i in range(1, n):
            if nums[i] > second:
                return True
            elif nums[i] > first:
                second = nums[i]
            else:
                first = nums[i]
        return False
# @lc code=end

