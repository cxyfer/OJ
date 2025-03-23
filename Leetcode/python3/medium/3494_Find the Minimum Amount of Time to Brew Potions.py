#
# @lc app=leetcode id=3494 lang=python3
#
# [3494] Find the Minimum Amount of Time to Brew Potions
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n = len(skill)
        avail = [0] * n
        for m in mana:
            # 假設開始時間就是上一輪第一個巫師的結束時間
            t = avail[0]
            # 根據每個巫師上一輪的結束時間和上一個巫師本輪的結束時間修正
            for i, (a, s) in enumerate(zip(avail, skill)):
                t = max(t, a) + s * m
            avail[n - 1] = t
            # 根據本輪最後一個巫師的結束時間往前修正
            for i in range(n - 2, -1, -1):
                avail[i] = avail[i + 1] - skill[i + 1] * m
        return t
# @lc code=end

sol = Solution()
print(sol.minTime([1,5,2,4], [5,1,4,2]))  # 110
print(sol.minTime([1,1,1], [1,1,1]))  # 5
print(sol.minTime([1,2,3,4], [1,2]))  # 21
print(sol.minTime([5], [8,3]))  # 55
