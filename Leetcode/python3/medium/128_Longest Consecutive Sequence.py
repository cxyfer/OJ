#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
1. 排序 + 分組循環
2. Hash Table
"""
# @lc code=start
class Solution1:
    def longestConsecutive(self, nums: List[int]) -> int:
        a = sorted(set(nums))
        n = len(a)
        ans = i = 0
        while i < n:
            st = i
            while i + 1 < n and a[i] + 1 == a[i + 1]:
                i += 1
            ans = max(ans, i - st + 1)
            i += 1
        return ans


class Solution2:
    def longestConsecutive(self, nums: List[int]) -> int:
        vis = set(nums)
        ans = 0
        for x in vis:
            if x - 1 in vis:
                continue
            y = x + 1
            while y in vis:
                y += 1
            ans = max(ans, y - x)
        return ans


# Solution = Solution1
Solution = Solution2
# @lc code=end

