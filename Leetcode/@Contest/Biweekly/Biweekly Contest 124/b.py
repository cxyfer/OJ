import math
from typing import *
from collections import *
from functools import lru_cache, cache
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        cnt = Counter(s)
        mx = max(cnt.values())
        target = [k for k, v in cnt.items() if v == mx] # 只保留出現次數最多的字母
        pos = defaultdict(int)
        for i, ch in enumerate(s): # 紀錄最後出現的位置
            if ch in target:
                pos[ch] = i
        lst = sorted(target, key=lambda x: pos[x]) # 按照最後出現的位置排序
        return "".join(lst)
    
sol = Solution()
print(sol.lastNonEmptyString("aabcbbca")) # ba
print(sol.lastNonEmptyString("abcd")) # abcd