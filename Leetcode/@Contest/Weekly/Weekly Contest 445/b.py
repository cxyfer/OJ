import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        cnt = Counter(s)
        ans = [''] * n
        idx = 0
        for ch, val in sorted(cnt.items()):
            if val & 1:
                ans[n//2] = ch
                val -= 1
            for _ in range((val + 1) // 2):
                ans[idx] = ch
                ans[n-1-idx] = ch
                idx += 1
        return ''.join(ans)



