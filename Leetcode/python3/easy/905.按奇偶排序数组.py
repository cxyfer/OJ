#
# @lc app=leetcode.cn id=905 lang=python3
#
# [905] 按奇偶排序数组
#
from en.Python3.mod.preImport import *
# @lc code=start
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        return sorted(nums, key=lambda x: x % 2)
# @lc code=end

