#
# @lc app=leetcode id=3880 lang=python3
#
# [3880] Minimum Absolute Difference Between Two Values
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
"""
由於題目要求的是最近的兩個 1 和 2 之間的距離，故對於每個 1 或 2，我們只需要關注上一個 2 或 1 的位置。
因此只需要一邊遍歷一邊維護最後出現的 1 和 2 的位置，並更新答案即可。
"""
class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        ans = float("inf")
        last1 = last2 = float("-inf")
        for i, x in enumerate(nums):
            if x == 1:
                ans = min(ans, i - last2)
                last1 = i
            elif x == 2:
                ans = min(ans, i - last1)
                last2 = i
        return ans if ans < float("inf") else -1
# @lc code=end

