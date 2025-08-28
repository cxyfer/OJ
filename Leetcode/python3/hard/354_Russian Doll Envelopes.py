#
# @lc app=leetcode id=354 lang=python3
#
# [354] Russian Doll Envelopes
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
二維 LIS
先對一個維度升序排序確保可以該維度構成 LIS，另外一個維度降序確保不會得到錯誤的結果。
對於 w 相同的若干個信封，如果按照 h 升序排序，則 (w, h2) 能接在 (w, h1) 的後面，
但由於他們的 w 相同，所以這樣會得到錯誤的結果，因此 h 需要降序排序。
"""
# @lc code=start
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # 先按照 w 升序排列，若 w 相同，則按照 h 降序排列
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        # f[i] 表示 長度為 i+1 的 LIS 的最後一個元素的最小值
        f = []
        for w, h in envelopes:
            idx = bisect_left(f, h)
            if idx == len(f):
                f.append(h)
            else:
                f[idx] = h
        return len(f)
# @lc code=end

