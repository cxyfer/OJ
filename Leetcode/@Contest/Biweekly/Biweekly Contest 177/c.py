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
有趣的題目

首先是一個很常見的套路，最終一定是只有 01 開頭或 10 開頭兩種可能，
而最優操作一定是略過不需要操作的位置，只對需要操作的位置進行一次+1或-1，因此操作次數其實是可以確定的。

那麼如何判斷操作後的最小極差呢？
可以反過來思考，如果某段值域區間包含了所有下標操作後的結果，那麼這個值域區間的差，就可以是操作後的極差。
而這其實就是滑動窗口找最短覆蓋區間，只是把值域跟下標調換而已。
"""


class Solution:
    def makeParityAlternating(self, nums: List[int]) -> List[int]:
        def helper(b: int) -> tuple:
            n = len(nums)
            ops = 0
            events = []
            for i, x in enumerate(nums):
                # 判斷是否需要變化，若需要的話可以變成 x - 1 或 x + 1
                if x & 1 != (i + b) & 1:
                    events.append((i, x - 1))
                    events.append((i, x + 1))
                    ops += 1
                else:
                    events.append((i, x))

            events.sort(key=lambda p: p[1])

            min_d = float("inf")
            left = have = 0
            cnt = [0] * n
            for right, (i, x) in enumerate(events):
                cnt[i] += 1
                if cnt[i] == 1:
                    have += 1
                while have == n:
                    j, y = events[left]
                    min_d = min(min_d, x - y)
                    cnt[j] -= 1
                    if cnt[j] == 0:
                        have -= 1
                    left += 1
            return ops, min_d

        return list(min(helper(0), helper(1)))


sol = Solution()
print(sol.makeParityAlternating([-2, -3, 1, 4]))  # [2,6]
print(sol.makeParityAlternating([0, 2, -2]))  # [1,3]
print(sol.makeParityAlternating([7]))  # [0,0]
