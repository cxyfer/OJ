from bisect import *
from collections import *
from functools import *
from heapq import *
from itertools import *
from math import *
from operator import *
from random import *
from string import *
from typing import *

"""
## Q2. 數學：等差數列和

如果當前的資源還缺少 d，則需要加 t = ceil(d / k) 個 k 才能滿足條件。
設當前加一個 k 的代價為 c，則這 t 個 k 的代價分別為 c, c + 1, ..., c + t - 1，
可以用等差數列和公式計算這 t 個 k 的總代價，其餘按題意模擬即可。
"""


MOD = int(1e9) + 7


class Solution:
    def minimumCost(self, nums: list[int], k: int) -> int:
        ans = 0
        cur = k
        c = 1
        for x in nums:
            if cur < x:
                # t = ceil((x - cur) / k)
                t = (x - cur + k - 1) // k
                cur += k * t
                ans += (c + c + t - 1) * t // 2
                ans %= MOD
                c += t
            cur -= x
        return ans


sol = Solution()
print(sol.canMakeSubsequence("cat", "chat"))  # Output: true
print(sol.canMakeSubsequence("plane", "apple"))  # Output: false
