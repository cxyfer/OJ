import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *


class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        cnt = Counter(s)
        ans = []
        ans.append(y * cnt[y])
        ans.append(x * cnt[x])
        del cnt[x]
        del cnt[y]
        for c, v in cnt.items():
            ans.append(c * v)
        return "".join(ans)
