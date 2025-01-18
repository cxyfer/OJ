#
# @lc app=leetcode.cn id=2943 lang=python3
#
# [2943] 最大化网格图中正方形空洞的面积
#
from preImport import *
# @lc code=start
class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hBars.sort()
        vBars.sort()

        def helper(bars):
            res = 1
            i = 0
            while i < len(bars) - 1:
                tmp = 1
                while i < len(bars) - 1 and bars[i] + 1 == bars[i + 1]:
                    tmp += 1
                    i += 1
                res = max(res, tmp)
                i += 1
            return res

        maxWidth = min(helper(hBars) + 1, helper(vBars) + 1)
        return pow(maxWidth, 2)
# @lc code=end

