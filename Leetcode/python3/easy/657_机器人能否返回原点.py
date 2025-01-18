#
# @lc app=leetcode.cn id=657 lang=python3
#
# [657] 机器人能否返回原点
#
from preImport import *
# @lc code=start
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        cnt = Counter(moves)
        return cnt["U"] == cnt["D"] and cnt["L"] == cnt["R"]
# @lc code=end

