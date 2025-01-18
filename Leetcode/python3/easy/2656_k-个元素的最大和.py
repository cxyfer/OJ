#
# @lc app=leetcode.cn id=2656 lang=python3
#
# [2656] K 个元素的最大和
#
from preImport import *
# @lc code=start
class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        return max(nums) * k + (k-1) * k // 2
# @lc code=end
sol = Solution()
print(sol.maximizeSum([1,2,3,4,5],3)) # 18
print(sol.maximizeSum([5,5,5],2)) # 11

