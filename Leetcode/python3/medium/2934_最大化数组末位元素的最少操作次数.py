#
# @lc app=leetcode.cn id=2934 lang=python3
#
# [2934] 最大化数组末位元素的最少操作次数
#
from typing import List
# @lc code=start
class Solution:
    """
        考慮兩種情況
        1. 換了最後一組
        2. 沒換最後一組
    """
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        def f(last1, last2):
            res = 0
            for x, y in zip(nums1, nums2):
                if x > last1 or y > last2:
                    if y > last1 or x > last2: # 不能換
                        return float('inf')
                    res += 1 # 可以換
            return res
        res1 = f(nums1[-1], nums2[-1])
        res2 = f(nums2[-1], nums1[-1])
        return min(res1, res2) if min(res1, res2) != float('inf') else -1
# @lc code=end

