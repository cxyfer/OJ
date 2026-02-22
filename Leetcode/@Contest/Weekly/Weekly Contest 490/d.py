import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *
from math import gcd


class Fraction:
    def __init__(self, num, dem=1):
        g = gcd(num, dem)
        self.num = num // g
        self.dem = dem // g

    def __eq__(self, other):
        return self.num == other.num and self.dem == other.dem

    def __add__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        return Fraction(
            (self.num * other.dem + other.num * self.dem),
            (self.num * other.num),
        )

    def __radd__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        return other + self

    def __sub__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        return Fraction(
            (self.num * other.dem - other.num * self.dem),
            (self.num * other.num),
        )

    def __rsub__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        return other - self

    def __mul__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        return Fraction(self.num * other.num, self.dem * other.dem)

    def __rmul__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        return other * self

    def __truediv__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        return Fraction(self.num * other.dem, self.dem * other.num)

    def __rtruediv__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        return other / self

    def __hash__(self):
        return hash((self.num, self.dem))

    def __str__(self):
        return f"{self.num}/{self.dem}"

    def __repr__(self):
        return f"Fraction({self.num}, {self.dem})"


class Solution:
    def countSequences(self, nums: List[int], k: int) -> int:
        def helper(nums):
            f = defaultdict(int)
            f[Fraction(1)] = 1
            for x in nums:
                nf = f.copy()
                for y, v in f.items():
                    nf[y * x] += v
                    nf[y / x] += v
                f = nf
            return f

        mid = len(nums) // 2
        L = helper(nums[:mid])
        R = helper(nums[mid:])

        ans = 0
        for x, v in R.items():
            ans += v * L[k / x]
        return ans


sol = Solution()
print(sol.countSequences([2, 3, 2], 6))  # 2
