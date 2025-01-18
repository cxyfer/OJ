#
# @lc app=leetcode.cn id=100116 lang=python3
#
# [100116] 找到冠军 II
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
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indeg = [0] * n
        for u, v in edges:
            indeg[v] += 1
        ans = -1
        for i in range(n):
            if indeg[i] == 0:
                if ans != -1:
                    return -1
                ans = i
        return ans
# @lc code=end

