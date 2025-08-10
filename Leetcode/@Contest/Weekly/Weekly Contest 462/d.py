import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

st = set()
odds = [-1, 1, 3, 5, 7, 9]
evens = [2, 4, 6, 8]
for i in range(1 << len(evens)):
    cur_evens = []
    for j in range(len(evens)):
        if (i >> j) & 1:
            cur_evens.append(evens[j])
    for odd in odds:
        digits = cur_evens + [odd] if odd != -1 else cur_evens
        if not digits:
            continue
        if len(digits) == 1:
            st.add(int(str(digits[0]) * digits[0]))
            continue
        s = sum(digits)
        if s > 16:
            continue
        cnt = defaultdict(int)
        for d in digits:
            cnt[d] += d // 2
        n = sum(cnt.values())
        def dfs(i, cur):
            if i == n:
                st.add(int(str(cur) + (str(odd) if odd != -1 else "") + str(cur)[::-1]))
                return
            for d in cnt:
                if cnt[d] == 0:
                    continue
                cnt[d] -= 1
                dfs(i + 1, cur * 10 + d)
                cnt[d] += 1
        dfs(0, 0)
ANS = sorted(st)

class Solution:
    def specialPalindrome(self, n: int) -> int:
        idx = bisect_right(ANS, n)
        return ANS[idx]
    
sol = Solution()
print(sol.specialPalindrome(2))  # 22
print(sol.specialPalindrome(33))  # 212