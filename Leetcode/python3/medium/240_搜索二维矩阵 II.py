#
# @lc app=leetcode.cn id=240 lang=python3
# @lcpr version=30108
#
# [240] 搜索二维矩阵 II
#


# @lcpr-template-start
import math
from math import *
from typing import *
from collections import *
from functools import *
from itertools import *
from bisect import *
from heapq import *
# @lcpr-template-end
# @lc code=start
class Solution:
    """
        Similar to 74. Search a 2D Matrix
        1. m Binary Search
        2. Abstract Binary Search Tree
    """
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return self.solveByABST(matrix, target)
    """
        2. Abstract Binary Search Tree
        將二維矩陣抽象成「以右上角為根的 BST」
        1. 若當前節點「大於」目標值，搜索當前節點的「左子樹」，也就是當前矩陣位置的「左方格子」，即 y--
        2. 若當前節點「小於」目標值，搜索當前節點的「右子樹」，也就是當前矩陣位置的「下方格子」，即 x++
        https://leetcode.cn/problems/search-a-2d-matrix/solutions/688573/gong-shui-san-xie-yi-ti-shuang-jie-er-fe-l0pq/
    """
    def solveByABST(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        x, y = 0, n - 1
        while x < m and y >= 0: # 保證不越界
            if matrix[x][y] > target:
                y -= 1
            elif matrix[x][y] < target:
                x += 1
            else: # matrix[x][y] == target
                return True
        return False
        
# @lc code=end



#
# @lcpr case=start
# [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]\n5\n
# @lcpr case=end

# @lcpr case=start
# [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]\n20\n
# @lcpr case=end

#

