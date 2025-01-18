#
# @lc app=leetcode.cn id=2971 lang=python3
#
# [2971] 找到最大周长的多边形
#
from preImport import *
# @lc code=start
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        # pre = list(accumulate(nums, initial=0))
        s = sum(nums)
        for i in range(n - 1, 1, -1):
            # if pre[i] > nums[i]:
            #     return pre[i] + nums[i]
            if s  > 2 * nums[i]: # s - nums[i] > nums[i]
                return s
            s -= nums[i]
        return -1
# @lc code=end

