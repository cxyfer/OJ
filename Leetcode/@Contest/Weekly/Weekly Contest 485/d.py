import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

class Solution:
    def lexSmallestAfterDeletion(self, s: str) -> str:
        cnt = defaultdict(int)
        suf = Counter(s)
        st = []
        for ch in s:
            suf[ch] -= 1
            while st and st[-1] > ch and (cnt[st[-1]] > 1 or suf[st[-1]] > 0):
                cnt[st.pop()] -= 1
            st.append(ch)
            cnt[ch] += 1
        while st and cnt[st[-1]] > 1:
            cnt[st.pop()] -= 1
        return ''.join(st)

sol = Solution()
print(sol.lexSmallestAfterDeletion("aaccb"))  # "aacb"
print(sol.lexSmallestAfterDeletion("abcab"))  # "abc"
print(sol.lexSmallestAfterDeletion("bbcac"))  # "bac"
print(sol.lexSmallestAfterDeletion("bcacb"))  # "acb"