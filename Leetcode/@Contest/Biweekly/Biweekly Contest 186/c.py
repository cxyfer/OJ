import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *
from math import inf

"""
## Q3. 貪心 + 分類討論？

首先注意到對於長度為 2 的字串可以任意轉換：`01/10 => 11 => 00 => 01/10 => 11`
1. `00 => 01/10 => 11`
2. `01 => 11 => 00 => 01/10 => 11`
3. `10 => 11 => 00 => 01/10 => 11`
4. `11 => 00 => 01/10 => 11`
因此只有當長度為 1 且 s1 = 1, s2 = 0 時無法轉換，其他情況都可以轉換。
可以暴力或用 Floyd-Warshall 預處理出所有長度為 2 的字串之間的最短轉換次數。

然後在保持前綴正確且不更動的前提下，對於每個位置 i 分類討論：
- 如果 s1[i] = s2[i]，則不需要操作；
- 如果 s1[i] = 0, s2[i] = 1，則需要 1 次操作將 s1[i] 變為 1；
- 如果 s1[i] = 1, s2[i] = 0，則需要考慮 s1[i+1]：
  - 如果 s1[i+1] = 1，則可以將 s1[i], s1[i+1] 變為 00，需要 1 次操作；
  - 如果 s1[i+1] = 0，則需要先將 s1[i+1] 變為 1，變成上述情況，需要 2 次操作；
- 如果 i = n-1，則需要考慮 s1[n-2], s1[n-1] 與 s2[n-2], s2[n-1] 的長度為 2 的字串之間的最短轉換次數，即前述預處理的結果。
"""

dist = [[inf] * 4 for _ in range(4)]
dist[3][0] = 1
for u in range(4):
    dist[u][u] = 0
    for b in range(2):
        v = u | (1 << b)
        if u ^ v:
            dist[u][v] = 1
for i in range(4):
    for j in range(4):
        for k in range(4):
            dist[j][k] = min(dist[j][k], dist[j][i] + dist[i][k])


class Solution:
    def minOperations(self, s1: str, s2: str) -> int:
        if s1 == s2:
            return 0

        n = len(s1)
        s1, s2 = list(map(int, s1)), list(map(int, s2))

        if n == 1 and s1[0] == 1 and s2[0] == 0:
            return -1

        ans = 0
        for i, (ch1, ch2) in enumerate(zip(s1, s2)):
            if ch1 == ch2:
                continue
            if ch1 == 0 and ch2 == 1:
                s1[i] = 1
                ans += 1
            elif i + 1 < n:
                if s1[i + 1] == 1:
                    s1[i] = s1[i + 1] = 0
                    ans += 1
                else:
                    s1[i] = 0
                    ans += 2
            else:
                a = (s1[-2] << 1) | s1[-1]
                b = (s2[-2] << 1) | s2[-1]
                ans += dist[a][b]
        return ans


sol = Solution()
print(sol.minOperations("11", "00"))  # 1
print(sol.minOperations("01", "10"))  # 3
print(sol.minOperations("1", "0"))  # -1
print(sol.minOperations("11", "01"))  # 2
print(sol.minOperations("111", "110"))  # 2
