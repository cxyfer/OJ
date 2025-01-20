#
# @lc app=leetcode id=2661 lang=python3
# @lcpr version=30204
#
# [2661] First Completely Painted Row or Column
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
    Hash Table
    每個元素都是唯一的，所以可以用 Hash Table 來記錄每個元素出現的位置
"""
# @lc code=start
class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        tbl = [None] * (m * n + 1)
        for i, row in enumerate(mat):   
            for j, val in enumerate(row):
                tbl[val] = (i, j)
        rows, cols = [0] * m, [0] * n # 紀錄每個 row 和 col 的塗色狀況
        for i, val in enumerate(arr):
            x, y = tbl[val]
            rows[x] += 1
            cols[y] += 1
            if rows[x] == n or cols[y] == m: # 如果這個 row 或 col 已經塗滿了，就回傳
                return i
        return -1  
# @lc code=end



#
# @lcpr case=start
# [1,3,4,2]\n[[1,4],[2,3]]\n
# @lcpr case=end

# @lcpr case=start
# [2,8,7,4,1,3,5,6,9]\n[[3,2,5],[1,4,6],[8,7,9]]\n
# @lcpr case=end

#

