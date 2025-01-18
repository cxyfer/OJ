#
# @lc app=leetcode.cn id=2594 lang=python3
#
# [2594] 修车的最少时间
#
from en.Python3.mod.preImport import *
# @lc code=start
class Solution:
    """
        Binary Search
    """
    def repairCars(self, ranks: List[int], cars: int) -> int:
        left = 0 # 下界
        right = min(ranks) * cars * cars # 上界
        while left < right - 1:
            mid = (left + right) // 2
            if sum(int(math.sqrt(mid // r)) for r in ranks) >= cars:
                right = mid
            else:
                left = mid
        return right
# @lc code=end


