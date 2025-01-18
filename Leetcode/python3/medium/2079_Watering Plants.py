#
# @lc app=leetcode id=2079 lang=python3
#
# [2079] Watering Plants
#
# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    """
        Simulation
    """
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        cur = capacity # 當前水壺的水量
        ans = 0
        for i, x in enumerate(plants):
            ans += 1
            if cur < x: # 水不夠，要補滿
                cur = capacity
                ans += i * 2
            cur -= x
        return ans
# @lc code=end

