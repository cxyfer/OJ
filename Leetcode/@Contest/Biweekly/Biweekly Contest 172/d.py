import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

class Solution:
    def lastInteger(self, n: int) -> int:
        ans = d = 1
        flag = 0  # 0: 從左到右刪除，1: 從右到左刪除
        while n > 1:
            if flag and n & 1 == 0:  # 第一個元素被刪掉了，移動下一個元素的位置
                ans += d
            n -= n >> 1  # 刪除一半的元素
            d <<= 1  # 每次刪除一半的元素，所以距離增加一倍
            flag ^= 1
        return ans

sol = Solution()
print(sol.lastInteger(5))  # 1