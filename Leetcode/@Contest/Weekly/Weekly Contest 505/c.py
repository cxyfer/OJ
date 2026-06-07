import math
from math import *
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

"""
Q3: 單調隊列優化DP

首先可以寫出以下轉移式：
f[i][k] = max(f[i - 1][k], max(f[j][k - 1] + s[i] - s[j]))
但狀態數量為 O(nm)，轉移需要 O(n)，總複雜度 O(n^2 m)，會超時。

考慮如何優化，可以將 i 有關的項提取出來後，從 max 下手：
f[i][k] = max(f[i - 1][k], s[i] + max(f[j][k - 1] - s[j]))
如果能維護區間內的最大值是經典技巧，可以參考後續類題。
具體來說，只要維護符合 j 在 [i - r, i - l] 範圍內的單調遞減隊列，即可優化掉轉移中的 max，總複雜度 O(nm)。

Similar problems: 
- 1871. Jump Game VII
- P1725 琪露诺
"""


class Solution:
    def maximumSum(self, nums: List[int], m: int, l: int, r: int) -> int:
        n = len(nums)
        s = list(accumulate(nums, initial=0))

        ans = -inf
        f = [0] * (n + 1)
        for k in range(1, m + 1):
            nf = [-inf] * (n + 1)
            q = deque()
            for i in range(1, n + 1):
                nf[i] = nf[i - 1]

                j = i - l
                if j >= 0:
                    vj = f[j] - s[j]
                    while q and (f[q[-1]] - s[q[-1]]) <= vj:
                        q.pop()
                    q.append(j)

                while q and q[0] < i - r:
                    q.popleft()

                if q:
                    nf[i] = max(nf[i], s[i] + (f[q[0]] - s[q[0]]))

            ans = max(ans, nf[n])
            f = nf
        return ans
