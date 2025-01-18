#
# @lc app=leetcode.cn id=1743 lang=python3
# @lcpr version=30108
#
# [1743] 从相邻元素对还原数组
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
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        n = len(adjacentPairs) + 1
        tbl = defaultdict(list)
        for x, y in adjacentPairs:
            tbl[x].append(y)
            tbl[y].append(x)
        st = -1
        for k, v in tbl.items():
            if len(v) == 1:
                st = k
                break
        ans = [0] * n
        ans[0] = st
        ans[1] = tbl[st][0]
        for i in range(2, n):
            for x in tbl[ans[i-1]]:
                if x != ans[i-2]:
                    ans[i] = x
                    break
        return ans
# @lc code=end



#
# @lcpr case=start
# [[2,1],[3,4],[3,2]]\n
# @lcpr case=end

# @lcpr case=start
# [[4,-2],[1,4],[-3,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[100000,-100000]]\n
# @lcpr case=end

#

