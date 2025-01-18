#
# @lc app=leetcode id=1380 lang=python3
# @lcpr version=30204
#
# [1380] Lucky Numbers in a Matrix
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
"""
    1. 預處理，找出每一橫列的最小值和每一直行的最大值
    2. Lucky number 最多只會有一個
        如果存在，則一定是每一橫列中的最小值其中的最大值，檢查其是否為該直行的最大值即可
"""
class Solution1:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        row_mn = [float("inf")] * m
        col_mx = [float("-inf")] * n
        for i, row in enumerate(matrix):
            for j, x in enumerate(row):
                row_mn[i] = min(row_mn[i], x)
                col_mx[j] = max(col_mx[j], x)
        ans = []
        for i, row in enumerate(matrix):
            for j, x in enumerate(row):
                if x == row_mn[i] and x == col_mx[j]:
                    ans.append(x)
        return ans
    
class Solution2:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        row_mx, idx = -float("inf"), 0
        for i, row in enumerate(matrix):
            k = 0
            mn = float("inf")
            for j, x in enumerate(row):
                if x < mn:
                    mn, k = x, j
            if mn > row_mx:
                row_mx, idx = mn, k
        return [row_mx] if all(row[idx] <= row_mx for row in matrix) else []

# class Solution(Solution1):
class Solution(Solution2):
    pass
# @lc code=end
