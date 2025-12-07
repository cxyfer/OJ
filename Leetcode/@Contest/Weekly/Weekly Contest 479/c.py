import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *
from sortedcontainers import SortedList

"""
Q3. 枚舉右維護左
對於每個 r ，可以計算有多少個 s[l - 1] 可以使 hp - (s[r] - s[l - 1]) >= req[r]
移項得 s[l - 1] >= s[r] + req[r] - hp，使用有序容器維護 s[l - 1] ，每次二分查找即可
"""

class Solution:
    def totalScore(self, hp: int, damage: List[int], requirement: List[int]) -> int:
        # s = list(accumulate(damage, initial = 0))
        # 有多少個 s[l - 1] 可以使 hp - (s[r] - s[l - 1]) >= req[r]
        # 移項得 s[r] + req[r] - hp <= s[l - 1]
        ans = 0
        sl = SortedList([0])
        s = 0
        for r, (x, y) in enumerate(zip(damage, requirement)):
            s += x
            idx = sl.bisect_left(s + y - hp)
            ans += len(sl) - idx
            sl.add(s)
        return ans

sol = Solution()
print(sol.totalScore(11, [3,6,7], [4,2,5]))  # 3
print(sol.totalScore(2, [10000,1], [1,1]))  # 1

"""
1 1 0
  1 0
    0
"""