#
# @lc app=leetcode.cn id=2009 lang=python3
#
# [2009] 使数组连续的最少操作数
#
from preImport import *
# @lc code=start
class Solution:
    """
        Sliding window
    """
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(set(nums)) # remove duplicates, and sort
        m, left = len(nums), 0
        for i in range(m):
            if nums[i] - nums[left] >= n: # 確保窗口內的數字都在 [nums[left], nums[left]+n) 之間
                left += 1
        return n - (m - left) # n - m + left

# @lc code=end
sol = Solution()
print(sol.minOperations([4,2,5,3])) # 0
print(sol.minOperations([1,2,3,5,6])) # 1
print(sol.minOperations([1,10,100,1000])) # 3

