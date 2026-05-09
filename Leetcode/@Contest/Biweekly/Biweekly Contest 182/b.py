import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

"""
Q2: ||分類討論||
本題要求子序列中不能包含 110 或 011。

首先注意到對於數列中的 0，其左側和右側都不能出現兩個 1，
這意味著如果 s 中有 0 的話，那麼 0 的左側和右側各最多只有 1 個 1，且這兩個 1 如果都出現的話，只能在最兩側，否則會有其他的 0 不滿足條件。

因此只有四種情況：
1. 沒有 1，即全部都是 0
2. 有一個 1
3. 有兩個 1，此時 1 必須在最兩側
4. 沒有 0，即全部都是 1
分別考慮操作次數即可。
"""

class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        cnt1 = s.count('1')
        cnt0 = n - cnt1

        ans = min(cnt0, cnt1, cnt1 - 1)
        ans = min(ans, (s[0] != '1') + (s[-1] != '1') + sum(s[i] != '0' for i in range(1, n - 1)))
        return max(0, ans)

sol = Solution()
print(sol.minFlips("1010"))  # 1
print(sol.minFlips("0110"))  # 1
print(sol.minFlips("1000"))  # 0
print(sol.minFlips("1111"))  # 0

