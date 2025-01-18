#
# @lc app=leetcode.cn id=1732 lang=python3
#
# [1732] 找到最高海拔
#
from en.Python3.mod.preImport import *
# @lc code=start
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefix = [0]
        for i in gain:
            prefix.append(prefix[-1] + i)
        return max(prefix)
# @lc code=end

