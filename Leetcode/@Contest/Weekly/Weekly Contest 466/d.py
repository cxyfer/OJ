import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

class Solution:
    def countBinaryPalindromes(self, n: int) -> int:
        s = bin(n)[2:]
        m = len(s)
        # 初始化 0 的貢獻
        ans = 1  
        # 考慮 [1, m - 1] 位數的回文，首位是 1，其餘位可以是任意數字
        for ln in range(1, m):
            ans += 1 << ((ln + 1) // 2 - 1)
        # 考慮 m 位數的回文，其前半部分可以是 [10...0, s[:k] - 1]
        k = (m + 1) // 2
        ans += int(s[:k], 2) - (1 << (k - 1))
        # 最後考慮前半部分是 s[:k] 的回文是否滿足條件
        ans += int(s[:k] + s[:m // 2][::-1], 2) <= n
        return ans

sol = Solution()
print(sol.countBinaryPalindromes(9))  # 6
print(sol.countBinaryPalindromes(0))  # 1
print(sol.countBinaryPalindromes(1))  # 2
print(sol.countBinaryPalindromes(20))  # 8