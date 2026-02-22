import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *


class Solution:
    def maximumXor(self, s: str, t: str) -> str:
        cnt = Counter(int(ch) for ch in t)
        ans = []
        for ch in s:
            c = int(ch)
            if cnt[c ^ 1]:
                ans.append(1)
                cnt[c ^ 1] -= 1
            else:
                ans.append(0)
                cnt[c] -= 1
        return "".join(map(str, ans))
