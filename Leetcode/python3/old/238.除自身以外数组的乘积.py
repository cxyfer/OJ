#
# @lc app=leetcode.cn id=238 lang=python3
#
# [238] 除自身以外数组的乘积
#
from en.Python3.mod.preImport import *
# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        left, right = 1, 1
        for i in range(n): 
            ans[i] *= left 
            left *= nums[i] # update left product
            j = n - 1 - i
            ans[j] *= right
            right *= nums[j] # update right product
        return ans
# @lc code=end

