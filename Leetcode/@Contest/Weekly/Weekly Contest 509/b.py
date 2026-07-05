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
## Q2. ||前後綴分解||

令 pre[i] 表示 s[0...i] 這段前綴，可以在 t 中匹配到的最早結尾位置；suf[i] 表示 s[i...n-1] 這段後綴，可以在 t 中匹配到的最晚開頭位置。

則可以枚舉修改位置 i，若 pre[i-1] 和 suf[i+1] 中間有空隙，表示可以透過修改 s[i] 使得整個 s 可以匹配到 t。
"""


class Solution:
    def canMakeSubsequence(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)

        if n == 1:
            return True

        pre = [m] * n
        j = 0
        for i, ch in enumerate(s):
            while j < m and t[j] != ch:
                j += 1
            if j >= m:
                break
            pre[i] = j
            j += 1

        suf = [-1] * n
        j = m - 1
        for i in range(n - 1, -1, -1):
            ch = s[i]
            while j >= 0 and t[j] != ch:
                j -= 1
            if j < 0:
                break
            suf[i] = j
            j -= 1

        # 修改第一個或最後一個字元，這需要匹配到該字元時，t 中還有沒匹配到的字元
        if suf[1] > 0 or pre[-2] < m - 1:
            return True

        # 枚舉修改位置 i，若 pre[i-1] 和 suf[i+1] 中間有空隙，表示可以透過修改 s[i] 使得整個 s 可以匹配到 t。
        for i in range(1, n - 1):
            if pre[i - 1] + 1 < suf[i + 1]:
                return True
        return False


sol = Solution()
print(sol.canMakeSubsequence("cat", "chat"))  # Output: true
print(sol.canMakeSubsequence("plane", "apple"))  # Output: false
