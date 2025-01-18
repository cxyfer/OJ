#
# @lc app=leetcode.cn id=977 lang=python3
#
# [977] 有序数组的平方
#
from en.Python3.mod.preImport import *
# @lc code=start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # Two pointers
        left, right = 0, n - 1
        idx = right # idx 指向ans的最後一個位置
        ans = [0] * n
        while(left <= right):
            if abs(nums[left]) < abs(nums[right]):
                ans[idx] = nums[right] **2
                right -= 1
            else:
                ans[idx] = nums[left] **2
                left +=1
            idx -= 1
        return ans
# @lc code=end

