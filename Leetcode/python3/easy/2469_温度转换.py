2#
# @lc app=leetcode.cn id=2469 lang=python3
#
# [2469] 温度转换
#
from typing import *
# @lc code=start
class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        return [celsius+273.15, celsius*1.8 + 32]
# @lc code=end

