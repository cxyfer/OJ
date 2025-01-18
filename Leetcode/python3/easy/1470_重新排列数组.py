#
# @lc app=leetcode.cn id=1470 lang=python3
#
# [1470] 重新排列数组
#
from preImport import *
# @lc code=start
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        for i in range(n):
            ans.append(nums[i])
            ans.append(nums[i+n])
        return ans
# @lc code=end

