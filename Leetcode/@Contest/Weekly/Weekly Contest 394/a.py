import math
from typing import *
from collections import *
from functools import lru_cache, cache
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        ans = 0
        cnt = Counter(word)
        for ch in cnt:
            if 'a' <= ch <= 'z' and ch.upper() in cnt:
                ans += 1
        return ans