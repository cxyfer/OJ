#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#
from preImport import *
# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last = dict()
        for i, x in enumerate(nums):
            if x in last and i - last[x] <= k:
                return True
            last[x] = i
        return False
# @lc code=end

