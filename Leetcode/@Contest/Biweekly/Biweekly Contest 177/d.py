import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

"""
設總共有 m = r - l + 1 種數字。
則若在第 d 位上，選擇數字 v，則剩餘位有 m^(k - 1) 種可能，因此貢獻為 v * m^(k - 1) * 10^d。
那麼可以得到所有數字在所有位數上的總貢獻為：
sum(10^d * m^(k - 1) * (l + ... + r) for d in range(k))
提出與 d 無關的部分：
m^(k - 1) * s * sum(10^d for d in range(k))
使用等比數列公式化簡一下：
m^(k - 1) * s * (10^k - 1) / (10 - 1)

本質國高中數學，只是用了乘法反元素就能評上 Hard ？
"""

MOD = int(1e9 + 7)

class Solution:
    def sumOfNumbers(self, l: int, r: int, k: int) -> int:
        m = r - l + 1
        s = (l + r) * (r - l + 1) // 2

        ans = pow(m, k - 1, MOD) * s % MOD
        ans *= pow(10, k, MOD) - 1
        ans *= pow(9, -1, MOD)
        return ans % MOD