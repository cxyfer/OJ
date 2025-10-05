#
# @lc app=leetcode id=3702 lang=python3
#
# [3702] Longest Subsequence With Non-Zero Bitwise XOR
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
腦筋急轉彎
- 若 nums 的 XOR 不為 0，則直接選全部元素即可
- 否則，如果 nums 中包含非 0 元素，則去除任意一個非 0 元素即可
"""
# @lc code=start
class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n = len(nums)
        if reduce(xor, nums) != 0:
            return n
        return n - 1 if any(x != 0 for x in nums) else 0
# @lc code=end

