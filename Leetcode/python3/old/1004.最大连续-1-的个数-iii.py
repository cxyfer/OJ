#
# @lc app=leetcode.cn id=1004 lang=python3
#
# [1004] 最大连续1的个数 III
#
from en.Python3.mod.preImport import *
# @lc code=start
class Solution:
    """
        Sliding window
        將題目轉換成找一個最長的子串，使得子串中0的個數不超過k個
    """
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = right = 0
        zeros = 0
        ans = 0
        while right < n:
            if nums[right] == 0:
                zeros += 1
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            ans = max(ans, right - left + 1)
            right += 1
        return ans
# @lc code=end
sol = Solution()
print(sol.longestOnes([1,1,1,0,0,0,1,1,1,1,0],2)) # 6
print(sol.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1],3)) # 10
print(sol.longestOnes([0,0,0,1],4)) # 4