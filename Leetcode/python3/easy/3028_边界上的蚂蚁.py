#
# @lc app=leetcode.cn id=3028 lang=python3
#
# [3028] 边界上的蚂蚁
#
from preImport import *
# @lc code=start
class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        ans = 0
        cur = 0
        for x in nums:
            cur += x
            if cur == 0:
                ans += 1
        return ans
# @lc code=end

