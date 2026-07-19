import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

"""
Q3: 逆序對

> 前置知識
> 透過交換相鄰元素使得數列有序的最少交換次數，等於逆序對的數量。

將 < a 的元素視為 0，> b 的元素視為 2，介於 a 與 b 之間的元素視為 1，則我們要將數列變成 [0, 1, 2] 的形式。
正常情況下統計逆序對需要 BIT 來輔助，但本題轉換後的值域範圍只有 [0, 1, 2]，因此可以直接統計每個元素前面有多少個比它大的元素即可。

"""

MOD = int(1e9) + 7

class Solution:
    def minAdjacentSwaps(self, nums: list[int], a: int, b: int) -> int:
        nums = [0 if x < a else (2 if x > b else 1) for x in nums]

        ans = 0
        cnt = [0] * 3
        for x in nums:
            if x == 0:
                ans += cnt[1] + cnt[2]
            elif x == 1:
                ans += cnt[2]
            cnt[x] += 1
        return ans % MOD