import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

"""
Q3. 前綴和
注意到操作 2 由於數列嚴格遞增的特性，因此可以拆分後的代價不變，因此從 li 到 ri 可以視為是一步一步走的。
那麼我們可以令 R[i] 表示從 i 到 i + 1 的代價，L[i] 表示從 i + 1 到 i 的代價，
則答案即為 sum(R[li:ri]) 或 sum(L[ri:li])，對 R 和 L 。
注意下標
"""


class Solution:
    def minCost(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        n = len(nums)
        R = [0] * n
        for i in range(n - 1):
            if i == 0 or nums[i] - nums[i - 1] > nums[i + 1] - nums[i]:
                R[i] = 1
            else:
                R[i] = nums[i + 1] - nums[i]
        L = [0] * n
        for i in range(n - 1, 0, -1):
            if i == n - 1 or nums[i] - nums[i - 1] <= nums[i + 1] - nums[i]:
                L[i] = 1
            else:
                L[i] = nums[i] - nums[i - 1]

        sr = list(accumulate(R, initial=0))
        sl = list(accumulate(L[::-1], initial=0))[::-1]

        ans = []
        for l, r in queries:
            if l <= r:
                ans.append(sr[r] - sr[l])
            else:
                ans.append(sl[r + 1] - sl[l + 1])
        return ans
