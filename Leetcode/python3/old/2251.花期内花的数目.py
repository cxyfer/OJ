#
# @lc app=leetcode.cn id=2251 lang=python3
#
# [2251] 花期内花的数目
#
from en.Python3.mod.preImport import *
# @lc code=start
class Solution:
    """
        Binary Search
    """
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        starts = sorted([start for start, _ in flowers])
        ends = sorted([end for _, end in flowers])
        return [bisect_right(starts, p) - bisect_left(ends, p) for p in people]
# @lc code=end

