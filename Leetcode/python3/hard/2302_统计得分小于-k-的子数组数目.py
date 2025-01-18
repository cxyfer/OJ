#
# @lc app=leetcode.cn id=2302 lang=python3
#
# [2302] 统计得分小于 K 的子数组数目
#
from preImport import *
# @lc code=start
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        left = 0
        s = 0
        for right in range(n): # 枚舉右端點
            s += nums[right]
            while s * (right - left + 1) >= k:
                s -= nums[left]
                left += 1
            ans += right - left + 1 # 以 right 為右端點，且滿足條件的子陣列數量
        return ans
# @lc code=end
[2,1,4,3,5]
10
sol = Solution()
print(sol.countSubarrays([2,1,4,3,5],10)) # 6

