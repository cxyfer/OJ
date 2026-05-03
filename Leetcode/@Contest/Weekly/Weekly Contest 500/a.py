import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

"""
Q1. 枚舉左維護右
注意本次需要對 i < j 的 i 計算答案，因此可以維護右側的 j 中奇數和偶數的數量，
當枚舉到 i 時，答案即為右側與 nums[i] 奇偶性不同的元素數量。
"""
class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        n = len(nums)
        cnt = [0, 0]
        ans = [0] * n
        for i in range(n - 1, -1, -1):
            x = nums[i]
            ans[i] = cnt[x & 1 ^ 1]
            cnt[x & 1] += 1
        return ans