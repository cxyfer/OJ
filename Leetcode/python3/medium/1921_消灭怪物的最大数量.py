#
# @lc app=leetcode.cn id=1921 lang=python3
#
# [1921] 消灭怪物的最大数量
#
from preImport import *
# @lc code=start
class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        arrivalTimes = sorted([math.ceil(d/s) for d, s in zip(dist, speed)])
        for attackTime, arrivalTime in enumerate(arrivalTimes):
            if arrivalTime <= attackTime: # 來不及消滅
                return attackTime
        return len(arrivalTimes)
# @lc code=end

