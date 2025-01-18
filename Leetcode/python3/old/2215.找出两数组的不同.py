#
# @lc app=leetcode.cn id=2215 lang=python3
#
# [2215] 找出两数组的不同
#
from en.Python3.mod.preImport import *
# @lc code=start
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        cnt1 = Counter(nums1)
        cnt2 = Counter(nums2)
        res = [[],[]]
        for i in cnt1:
            if i not in cnt2:
                res[0].append(i)
        for i in cnt2:
            if i not in cnt1:
                res[1].append(i)
        return res
# @lc code=end

