#
# @lc app=leetcode.cn id=2661 lang=python3
#
# [2661] 找出叠涂元素
#
from preImport import *
# @lc code=start
class Solution:
    """
        Hash Table
        每個元素都是唯一的，所以可以用 Hash Table 來記錄每個元素出現的位置
    """
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        tbl = {} # 紀錄這個元素出現的位置
        for i in range(m):
            for j in range(n):
                tbl[mat[i][j]] = (i, j)
        rows, cols = [0]*m, [0]*n # 紀錄每個 row 和 col 的塗色狀況
        for i, val in enumerate(arr):
            x, y = tbl[val]
            rows[x] += 1
            cols[y] += 1
            if rows[x] == n or cols[y] == m: # 如果這個 row 或 col 已經塗滿了，就回傳
                return i
        return -1
# @lc code=end

