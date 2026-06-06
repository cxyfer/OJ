import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *
from typing import List

"""
## Q3: DP
題意：每個 token 可以選擇放置在當前位置、或前一個位置，最終的分數為所有被 token 擺放位置的分數之和，求最大分數。
注意如果有多個 token 擺放在同一個位置，分數**不會疊加**，因此不能直接貪心考慮。
另外由於 1 <= nums[i] <= 10^5，擺放是一定比不擺放能夠獲得更高的分數的，因此不需要考慮當可以擺放時選擇不擺放的情況。

可以注意到當考慮 i 的 token 是否擺放時，需要考慮 i - 1 上是否有 token，
因此可以令 f[i][0/1] 表示第 i 個位置上是否有 token 時的最大分數，0 表示有，1 表示沒有。
轉移時需要考慮前一個位置 j 的 token 擺放情況，轉移方程如下：
- f[i][0] = max(f[i - 1][0], f[i - 1][1]) + nums[i]  # 前一個位置是否擺放，當前位置都可以擺放
- f[i][1] = max(f[i - 1][0], f[i - 1][1] + nums[i - 1])  # 若前一個位置已經擺放了，則不可以擺放在前一個位置
"""


class Solution:
    def maxTotal(self, nums: List[int], s: str) -> int:
        ans = 0
        f0 = f1 = 0  # 第 i 個位置上是否有 token 時的最大分數，0 表示有，1 表示沒有
        for i, c in enumerate(s):
            if c == "1":
                f0, f1 = (
                    max(f0, f1) + nums[i],
                    max(f0, f1 + (nums[i - 1] if i > 0 else 0)),
                )
            else:
                f0 = f1 = max(f0, f1)
            ans = max(ans, max(f0, f1))
        return ans
