import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *
from typing import List

"""
和基本的打家劫舍相同，但原題是一律不偷相鄰的，這題是只有相鄰是相同顏色才不能偷。
"""


class Solution:
    def rob(self, nums: List[int], colors: List[int]) -> int:
        f0 = f1 = 0
        for i, x in enumerate(nums):
            if i > 0 and colors[i] == colors[i - 1]:
                f0, f1 = f1 + nums[i], max(f0, f1)
            else:
                f0, f1 = max(f0, f1) + nums[i], max(f0, f1)
        return max(f0, f1)
