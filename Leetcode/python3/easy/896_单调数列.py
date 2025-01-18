#
# @lc app=leetcode.cn id=896 lang=python3
#
# [896] 单调数列
#
from preImport import *
# @lc code=start
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)
        res1, res2 = True, True
        for i in range(1, n):
            if nums[i] < nums[i-1]:
                res1 = False
            if nums[i] > nums[i-1]:
                res2 = False
        return res1 or res2
# @lc code=end
sol = Solution()
# print(sol.isMonotonic([1,2,2,3])) # true
# print(sol.isMonotonic([6,5,4,4])) # true
# print(sol.isMonotonic([1,3,2])) # false
print(sol.isMonotonic([11,11,9,4,3,3,3,1,-1,-1,3,3,3,5,5,5])) # false
