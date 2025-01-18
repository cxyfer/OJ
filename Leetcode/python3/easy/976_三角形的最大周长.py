97#
# @lc app=leetcode.cn id=976 lang=python3
#
# [976] 三角形的最大周长
#
from preImport import *
# @lc code=start
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort(reverse=True)
        for i in range(n-2):
            if nums[i] < nums[i+1] + nums[i+2]:
                return nums[i] + nums[i+1] + nums[i+2]
        return 0
# @lc code=end

