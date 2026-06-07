import math
from math import inf
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

"""
Q4: WQS 二分 / Aliens Trick
對於這類「選擇 k 個元素使得某個函數最大化」的問題，可以考慮 WQS 二分（又稱 Aliens Trick）。
"""

class Solution:
    def maximumSum(self, nums: List[int], m: int, l: int, r: int) -> int:
        n = len(nums)
        s = list(accumulate(nums, initial=0))

        res1 = -inf
        q = deque()
        for i in range(1, n + 1):
            j = i - l
            if j >= 0:
                while q and s[q[-1]] >= s[j]:
                    q.pop()
                q.append(j)
            while q and q[0] < i - r:
                q.popleft()
            if q:
                res1 = max(res1, s[i] - s[q[0]])
        
        if res1 <= 0:
            return res1

        def check(p: int):
            f = [(0, 0)] * (n + 1)  # (value, count)

            q = deque()
            for i in range(1, n + 1):
                f[i] = f[i - 1]

                j = i - l
                if j >= 0:
                    while q and (f[q[-1]][0] - s[q[-1]], f[q[-1]][1]) <= (f[j][0] - s[j], f[j][1]):
                        q.pop()
                    q.append(j)

                while q and q[0] < i - r:
                    q.popleft()

                if q:
                    j = q[0]
                    f[i] = max(f[i], (f[j][0] + s[i] - s[j] - p, f[j][1] + 1))

            return f[n]

        if check(0)[1] <= m:
            return check(0)[0]

        left, right = 0, int(1e18)
        while left <= right:
            mid = (left + right) // 2
            _, cnt = check(mid)
            if cnt <= m:
                right = mid - 1
            else:
                left = mid + 1

        return check(right)[0] + right * m

sol = Solution()
print(sol.maximumSum([4,1,-5,2], 2, 1, 3))  # 7
print(sol.maximumSum([1,0,3,4], 2, 1, 2))  # 8
print(sol.maximumSum([-1,7,-4], 1, 2, 3))  # 6
print(sol.maximumSum([-3,-4,-1], 2, 1, 2))  # -1
print(sol.maximumSum([9,10,13], 2, 1, 3))  # 32