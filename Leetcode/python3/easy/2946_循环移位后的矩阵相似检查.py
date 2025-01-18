#
# @lc app=leetcode.cn id=2946 lang=python3
#
# [2946] 循环移位后的矩阵相似检查
#
from preImport import *
# @lc code=start
class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m, n = len(mat), len(mat[0])
        if k > n:
            k %= n
        for row in mat:
            if row[-k:] + row[:-k] != row:
                return False
        return True
# @lc code=end

