#
# @lc app=leetcode.cn id=2580 lang=python3
#
# [2580] 统计将重叠区间合并成组的方案数
#
from preImport import *
# @lc code=start
class Solution:
    """
        區間合併 + 離散數學
    """
    def countWays(self, ranges: List[List[int]]) -> int:
        MOD = 10**9 + 7
        ranges.sort(key=lambda x: x[0]) # 按左端點排序
        cnt, max_r = 0, -float('inf')
        for l, r in ranges:
            if l > max_r: # 若左端點大於前一區間的右端點，則無法合併
                cnt += 1
            max_r = max(max_r, r)
        return pow(2, cnt, MOD)
# @lc code=end

