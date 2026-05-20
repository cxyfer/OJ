import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

"""

Q2. 避免浮點數誤差的 r^(1/k) 作法，最壞為 sqrt(r)
||計算從 [l, r] 之間滿足特定條件的數字個數，等同於計算從 [0, r] 之間滿足特定條件的數字個數，減去從 [0, l-1] 之間滿足特定條件的數字個數||
||那麼求 [0, U] 之前滿足 x^k <= U 的 x 個數，等同於求滿足 x <= U^(1/k) 的 x 個數||
||但直接可能存在浮點數誤差，不過注意對於 k = 1 的情況 U + 1 即為答案，而對於 k > 1 的情況可以從 0 開始遞增 x，直到 x^k > U 為止，因此可以得到 r^(1/k) 的做法||
"""

class Solution:
    def countKthRoots(self, l: int, r: int, k: int) -> int:

        def calc(U):
            if U == 0:
                return 1
            if U < 0:
                return 0
            if k == 1:
                return U + 1
            res = 0
            while pow(res , k) <= U:
                res += 1
            return res

        return calc(r) - calc(l - 1)