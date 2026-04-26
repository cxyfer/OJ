import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = set("aeiou")

        cnt = defaultdict(int)
        pos = dict()
        for i, ch in enumerate(s):
            if ch in vowels:
                cnt[ch] += 1
                if ch not in pos:
                    pos[ch] = i
        keys = sorted(cnt.keys(), key=lambda x : (-cnt[x], pos[x]))

        ans = list(s)
        j = 0
        for i, ch in enumerate(s):
            if ch in vowels:
                ans[i] = keys[j]
                cnt[keys[j]] -= 1
                if cnt[keys[j]] == 0:
                    j += 1
        return ''.join(ans)