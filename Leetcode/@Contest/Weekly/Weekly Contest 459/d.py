import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from math import gcd, comb

"""
y = mx + k
m = dy / dx
k = y1 - m*x1 = (y1x2 - y1x1 - x1y2  + x1y1) / dx = (y1x2 - x1y2) / dx
"""
from fractions import Fraction
MOD = int(1e9 + 7)
class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        n = len(points)
        def get_line(x1: int, y1: int, x2: int, y2: int):
            dx = x2 - x1
            dy = y2 - y1
            # m = Fraction(dy, dx) if dx else "x"
            # k = y1 - m * x1 if dx else x1
            # return m, k
            k = y1 * x2 - x1 * y2
            g = gcd(dx, dy, k)
            dx //= g
            dy //= g
            k //= g
            if dx < 0 or dx == 0 and dy < 0:
                dx, dy, k = -dx, -dy, -k
            return (dx, dy), k
        # cnt[m][k] 為在 y = mx + k 直線上任取兩點的方法數
        cnt = defaultdict(lambda: defaultdict(int))
        # mp[m][k] 為在 y = mx + k 直線上的所有點，以下標表示
        mp = defaultdict(lambda: defaultdict(set))
        for i, (x1, y1) in enumerate(points):
            for j in range(i + 1, n):
                x2, y2 = points[j]
                m, k = get_line(x1, y1, x2, y2)
                cnt[m][k] += 1
                mp[m][k].add(i)
                mp[m][k].add(j)
        ans = 0
        # 和相同斜率的其他直線可以構成梯形
        for m, ks in cnt.items():
            s = 0
            for k, v in ks.items():
                ans += v * s
                s += v
        # 計算平行四邊形數量
        def cal(points):
            n = len(points)
            cnt = defaultdict(int)
            for i, (x1, y1) in enumerate(points):
                for j in range(i + 1, n):
                    x2, y2 = points[j]
                    cnt[(x1 + x2, y1 + y2)] += 1
            res = 0
            for v in cnt.values():
                if v >= 2:
                    res += comb(v, 2)
            return res
        # 減去重複計算的平行四邊形
        ans -= cal(points)
        for m, ks in mp.items():
            for k, idxs in ks.items():
                # 加回四點共線的情況
                ans += cal([points[i] for i in idxs])
        return ans % MOD

sol = Solution()
print(sol.countTrapezoids([[-3,2],[3,0],[2,3],[3,2],[2,-3]])) # 2
print(sol.countTrapezoids([[71,-89],[-75,-89],[-9,11],[-24,-89],[-51,-89],[-77,-89],[42,11]])) # 10
print(sol.countTrapezoids([[83,-25],[74,11],[-65,-25],[33,-25],[17,-25],[1,30],[-84,-25],[1,-25],[1,-92],[-87,13]])) # 0