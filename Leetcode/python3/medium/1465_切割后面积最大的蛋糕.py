#
# @lc app=leetcode.cn id=1465 lang=python3
#
# [1465] 切割后面积最大的蛋糕
#
from en.Python3.mod.preImport import *
# @lc code=start
class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        MOD = 10 ** 9 + 7
        h_cuts = [0] + sorted(horizontalCuts) + [h]
        w_cuts = [0] + sorted(verticalCuts) + [w]
        h_max = max(h_cuts[i] - h_cuts[i-1] for i in range(1, len(h_cuts)))
        w_max = max(w_cuts[i] - w_cuts[i-1] for i in range(1, len(w_cuts)))
        return h_max * w_max % MOD
# @lc code=end

