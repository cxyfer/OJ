#
# @lc app=leetcode id=3769 lang=python3
#
# [3769] Sort Integers by Binary Reflection
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
def f(x: int) -> int:
    y = 0
    while x:
        y = (y << 1) | (x & 1)
        x >>= 1
    return y

class Solution:
    def sortByReflection(self, nums: List[int]) -> List[int]:
        return sorted(nums, key = lambda x : (f(x), x))
# @lc code=end

