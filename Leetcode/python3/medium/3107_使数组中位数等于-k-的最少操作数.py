#
# @lc app=leetcode.cn id=3107 lang=python3
#
# [3107] 使数组中位数等于 K 的最少操作数
#
from preImport import *
# @lc code=start
class Solution:
    """
        Sort
        看範例即可
    """
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        m = n // 2
        ans = 0
        if nums[m] < k: # 讓中位數以右的數字增加至 k
            for i in range(m, n):
                if nums[i] >= k:
                    break
                ans += k - nums[i]
        elif nums[m] > k: # 讓中位數以左的數字減少至 k
            for i in range(m, -1, -1):
                if nums[i] <= k: 
                    break
                ans += nums[i] - k
        return ans
# @lc code=end
sol = Solution()
print(sol.minOperationsToMakeMedianK([2,5,6,8,5], 4)) # 2
print(sol.minOperationsToMakeMedianK([2,5,6,8,5], 7)) # 3
print(sol.minOperationsToMakeMedianK([1,2,3,4,5,6], 4)) # 0
