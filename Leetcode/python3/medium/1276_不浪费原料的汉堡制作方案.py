#
# @lc app=leetcode.cn id=1276 lang=python3
#
# [1276] 不浪费原料的汉堡制作方案
#
from preImport import *
# @lc code=start
class Solution:
    """
        Math 
        4x + 2y = tomatoSlices 
        x + y = cheeseSlices 

        x = (tomatoSlices - 2 * cheeseSlices) / 2
        y = (4 * cheeseSlices - tomatoSlices) / 2
    """
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        x = (tomatoSlices - 2 * cheeseSlices) / 2
        y = (4 * cheeseSlices - tomatoSlices) / 2
        if x < 0 or y < 0 or x != int(x) or y != int(y):
            return []
        return [int(x), int(y)]
 
# @lc code=end

