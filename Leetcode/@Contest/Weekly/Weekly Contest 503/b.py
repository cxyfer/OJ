import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *


class Solution:
    def passwordStrength(self, password: str) -> int:
        ans = 0
        vis = set()
        for ch in password:
            if ch in vis:
                continue
            vis.add(ch)
            if ord("a") <= ord(ch) <= ord("z"):
                ans += 1
            elif ord("A") <= ord(ch) <= ord("Z"):
                ans += 2
            elif ord("0") <= ord(ch) <= ord("9"):
                ans += 3
            elif ch in "!@#$":
                ans += 5
        return ans
