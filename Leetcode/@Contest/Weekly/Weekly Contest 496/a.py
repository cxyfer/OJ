import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

class Solution:
    def mirrorFrequency(self, s: str) -> int:
        cnt = Counter(s)
        ans = 0
        for i in range(26 // 2):
            ans += abs(cnt[chr(ord('a') + i)] - cnt[chr(ord('z') - i)])
        for i in range(10 // 2):
            ans += abs(cnt[chr(ord('0') + i)] - cnt[chr(ord('9') - i)])
        return ans