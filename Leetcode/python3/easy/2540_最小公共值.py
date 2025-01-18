#
# @lc app=leetcode.cn id=2540 lang=python3
#
# [2540] 最小公共值
#
from preImport import *
# @lc code=start
class Solution:
    """
        1. Set
        2. Two pointers
    """
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        # return self.solve1(nums1, nums2)
        return self.solve2(nums1, nums2)

    def solve1(self, nums1: List[int], nums2: List[int]) -> int:
        # return min(set(nums1) & set(nums2), default=-1)
        nums1 = set(nums1)
        for x in nums2:
            if x in nums1:
                return x
        return -1
    def solve2(self, nums1: List[int], nums2: List[int]) -> int:
        i, n = 0, len(nums1)
        for y in nums2:
            while i < n and nums1[i] < y: # 找到nums1[i] >= y
                i += 1
            if i < n and nums1[i] == y:
                return y
        return -1
# @lc code=end

