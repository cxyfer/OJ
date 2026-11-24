#
# @lc app=leetcode id=4120 lang=python3
#
# [4120] Count Dominant Elements
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
Weekly Contest 529 - Q1
按題目枚舉每個元素，判斷是否為 dominant element 即可。
注意特判 n = 1 的情況，以及處理首尾元素。
"""
# @lc code=start
class Solution:
    def countDominantElements(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        ans = 0
        for i in range(1, n - 1):
            if nums[i] * 2 >= nums[i - 1] + nums[i + 1]:
                ans += 1
        ans += int(nums[0] >= nums[1]) + int(nums[-1] >= nums[-2])
        return ans
# @lc code=end

