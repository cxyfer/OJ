#
# @lc app=leetcode id=4117 lang=python3
#
# [4117] Minimum Range After Sum Operations
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
Biweekly Contest 196 - Q2
數學

不失一般性，令 a <= b <= c
則分別選擇替換 a, b, c，經過一次操作後，排序後的結果可能為：
b   c   b+c    範圍為 (b+c) - b = c，新的次小值為 c
a   c   a+c    範圍為 (a+c) - a = c，新的次小值為 c
a   b   a+b    範圍為 (a+b) - a = b，新的次小值為 b

可以發現在經過一次操作後：
1. 三種情況的範圍皆 >= 操作前的中間值 b（其中替換 c 可達到最小值 b）。
2. 新三元組的次小值單調不減（新的次小值為 b 或 c，皆 >= b）。

由歸納法可知，經過任意 k >= 1 次操作，在第 k 次操作前的次小值必然 >= b，
因此第 k 次操作後的範圍必然 >= b，不可能比做一次操作得到的 b 更小。

綜合「不做操作（範圍為 c - a）」與「至少做一次操作（最小範圍為 b）」，
答案即為 min(c - a, b)。
"""
# @lc code=start
class Solution:
    def minRange(self, a: int, b: int, c: int) -> int:
        a, b, c= sorted((a, b, c))
        return min(c - a, b)
# @lc code=end