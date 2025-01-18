#
# @lc app=leetcode.cn id=2216 lang=python3
#
# [2216] 美化数组的最少删除数
#
from preImport import *
# @lc code=start
class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            if (i-ans) % 2 == 0 and i + 1 < n: # 最終的下標為i-ans，枚舉最終的偶數下標
                if nums[i] == nums[i+1]: # 連續兩個數字相同，刪去其一
                    ans += 1
        return ans if (n - ans) % 2 == 0 else ans+1 
# @lc code=end

