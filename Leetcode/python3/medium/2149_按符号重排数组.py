#
# @lc app=leetcode.cn id=2149 lang=python3
#
# [2149] 按符号重排数组
#
from preImport import *
# @lc code=start
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        pos, neg = 0, 0 # Two pointers
        for i in range(n//2):
            while pos < n and nums[pos] < 0:
                pos += 1
            while neg < n and nums[neg] > 0:
                neg += 1
            ans[i*2] = nums[pos]
            ans[i*2+1] = nums[neg]
            pos += 1
            neg += 1
        return ans
# @lc code=end

