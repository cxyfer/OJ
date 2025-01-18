#
# @lc app=leetcode.cn id=2352 lang=python3
#
# [2352] 相等行列对
#
from en.Python3.mod.preImport import *
# @lc code=start
class Solution:
    """
        Hash Map
        1. 對於每一列，計算其出現次數
        2. 再對於每一行檢查是否與某一列相等，若相等則加上該列出現次數
    """
    def equalPairs(self, grid: List[List[int]]) -> int:
        cnt = Counter([tuple(row) for row in grid])
        return sum(cnt[col] for col in zip(*grid))
# @lc code=end

