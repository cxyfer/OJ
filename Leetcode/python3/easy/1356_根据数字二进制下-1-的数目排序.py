#
# @lc app=leetcode.cn id=1356 lang=python3
#
# [1356] 根据数字二进制下 1 的数目排序
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
    def sortByBits(self, arr: List[int]) -> List[int]:
        dic = defaultdict(list)
        for i in arr:
            dic[bin(i).count('1')].append(i)
        return [x for key in sorted(dic.keys()) for x in sorted(dic[key])]
# @lc code=end

