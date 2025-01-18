import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        ln1, ln2 = len(s) // k, len(t) // k
        cnt1 = Counter([s[i:i+ln1] for i in range(0, len(s), ln1)])
        cnt2 = Counter([t[i:i+ln2] for i in range(0, len(t), ln2)])
        return cnt1 == cnt2