#
# @lc app=leetcode.cn id=2760 lang=python3
#
# [2760] 最长奇偶子数组
#
from preImport import *
# @lc code=start
class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        ans = 0
        i = 0
        while (i < n):
            if nums[i] > threshold or nums[i] % 2 != 0:
                i += 1 
                continue
            st = i # left
            i += 1 # right
            while i < n and nums[i] <= threshold and nums[i] % 2 != nums[i - 1] % 2:
                i += 1
            ans = max(ans, i - st)
        return ans
# @lc code=end

# @test([3,2,5,4],5)=3
# @test([1,2],2)=1
# @test([2,3,4,5],4)=3

sol = Solution()
print(sol.longestAlternatingSubarray([3,2,5,4],5)) # 3
print(sol.longestAlternatingSubarray([1,2],2)) # 1
print(sol.longestAlternatingSubarray([2,3,4,5],4)) # 3
print(sol.longestAlternatingSubarray([1],1)) # 0