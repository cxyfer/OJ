#
# @lc app=leetcode.cn id=274 lang=python3
#
# [274] H 指数
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
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        cnt = Counter([min(n, x) for x in citations])
        s = 0
        for i in range(n, -1, -1):
            s += cnt[i]
            if s >= i:
                return i
# @lc code=end

