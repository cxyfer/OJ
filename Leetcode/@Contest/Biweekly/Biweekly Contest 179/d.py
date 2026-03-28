import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

"""
## Q4: ||前綴和優化DP||

預先處理 [0, 5000] 內數字的 digit sum，並將數字按照 digit sum 分組。
令 groups[d] 表示 digit sum 為 d 的數字列表。

令 f[i][v] 表示考慮到第 i 個數字，且，最後一個數字為 v 時的合法陣列數量。
而當前位置的 digitSum[i] 為 d 時，則可以填入 groups[d] 中的數字。
對於 groups[d] 中的每個數字 x，只要 v <= x，則有 f[i][x] += f[i - 1][v] 的轉移。

但這樣的轉移對於每個數字都要遍歷一次 f 的值域，太慢了。
注意到我們轉移時只需要取 f 的前綴區間和，因此可以對 f 做前綴和來優化轉移過程。
"""

MOD = int(1e9 + 7)
MAX_V = int(5e3)

groups = defaultdict(list)
for x in range(MAX_V + 1):
    s = sum(int(d) for d in str(x))
    groups[s].append(x)

# print(max(len(lst) for lst in groups.values()))  # 365

class Solution:
    def countArrays(self, digitSum: list[int]) -> int:
        f = [0] * (MAX_V + 1)
        f[0] = 1
        for d in digitSum:
            s = list(accumulate(f, func=lambda x, y: x + y % MOD))
            nf = [0] * (MAX_V + 1)
            for x in groups[d]:
                nf[x] = (nf[x] + s[x]) % MOD
            f = nf
        return sum(f) % MOD


sol = Solution()
print(sol.countArrays(digitSum = [25,1]))  # 6
print(sol.countArrays(digitSum = [1]))  # 4
print(sol.countArrays(digitSum = [2,49,23]))  # 0groupsgroupsgroups