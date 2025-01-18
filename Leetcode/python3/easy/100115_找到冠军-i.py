#
# @lc app=leetcode.cn id=100115 lang=python3
#
# [100115] 找到冠军 I
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
    def findChampion(self, grid: List[List[int]]) -> int:
        n = len(grid)
        for j in range(n):
            flag = True
            for i in range(n):
                if grid[i][j] == 1:
                    flag = False
                    break
            if flag:
                return j
# @lc code=end

