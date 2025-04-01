#
# @lc app=leetcode id=3074 lang=python3
#
# [3074] Apple Redistribution into Boxes
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        s = sum(apple)
        capacity.sort(reverse=True)
        cur = 0
        for i, c in enumerate(capacity, 1):
            cur += c
            if cur >= s:
                return i
        return 0
# @lc code=end

