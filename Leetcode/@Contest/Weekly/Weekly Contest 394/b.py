import math
from typing import *
from collections import *
from functools import lru_cache, cache
from heapq import *
from bisect import *
from itertools import *

# 所有小寫的 c 都在第一個大寫 c 之前出現，那麼這個 c 就被稱為特殊字母。

"""
    根據範例，需要小寫和大寫都有，且小寫在大寫之前出現
"""
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        cnt = defaultdict(list)
        for i, c in enumerate(word):
            cnt[c].append(i)
        ans = 0
        for i in range(26):
            ch = chr(ord('a') + i)
            if ch not in cnt:
                continue
            if ch.upper() not in cnt:
                continue
            if all(idx < cnt[ch.upper()][0] for idx in cnt[ch]):
                ans += 1
        return ans
sol = Solution()
print(sol.numberOfSpecialChars("aaAbcBC")) # 3
print(sol.numberOfSpecialChars("abc")) # 0
print(sol.numberOfSpecialChars("AbBCab")) # 0