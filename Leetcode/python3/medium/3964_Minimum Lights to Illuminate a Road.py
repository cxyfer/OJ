#
# @lc app=leetcode id=3964 lang=python3
#
# [3964] Minimum Lights to Illuminate a Road
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
差分陣列 + 貪心
首先根據題意，需要根據給定的區間維護覆蓋狀態，自然而然可以想到差分陣列。
而額外增加的每個區間可以維護 3 個位置，基於貪心思想，一定是在第一個沒有被覆蓋的位置放置燈，這樣可以最大程度地覆蓋後續位置。
"""
# @lc code=start
class Solution:
    def minLights(self, lights: list[int]) -> int:
        n = len(lights)
        diff = [0] * (n + 1)  # 差分陣列
        for i, v in enumerate(lights):
            if v > 0:
                diff[max(i - v, 0)] += 1
                diff[min(i + v, n - 1) + 1] -= 1

        ans = s = 0
        for i in range(n):
            s += diff[i]
            if s == 0:  # 需要額外放置燈，放置在 i + 1 可以覆蓋 [i, i + 2]
                s += 1
                ans += 1
                diff[min(i + 2, n - 1) + 1] -= 1
        return ans
# @lc code=end

