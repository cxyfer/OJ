import math
from typing import *
from collections import *
from functools import lru_cache, cache
from heapq import *
from bisect import *
from itertools import *
import string

class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        n = len(s)

        @cache
        def f(ss, k):
            n = len(ss)
            if n == 0:
                return 0
            i = 0
            cnt = Counter()
            cnt[ss[i]] += 1
            while (len(cnt.keys()) <= k):
                i += 1
                if i >= n:
                    break
                cnt[ss[i]] += 1
            del cnt
            return 1 + f(ss[i:], k)
        def f2(ss, k, idx):
            n = len(ss)
            if n == 0:
                return 0
            i = 0
            cnt = Counter()
            cnt[ss[i]] += 1
            while (len(cnt.keys()) <= k):
                i += 1
                if i >= n:
                    break
                cnt[ss[i]] += 1
            del cnt
            if idx < i: # 改變的字母在左邊，可以用記憶化
                return 1 + f(ss[i:], k)
            else:
                return 1 + f2(ss[i:], k, idx-i)
        i = 0
        ans = f(s, k)
        while (i < n):
            cnt = Counter()
            avail = set(string.ascii_lowercase)
            cnt[s[i]] += 1
            avail.remove(s[i])
            while (len(cnt.keys()) <= k):
                if s[i] not in avail: # 這個字母已經用過了，考慮換成其他字母
                    for ch in avail:
                        ans = max(ans, f2(s[:i] + ch + s[i+1:], k, i))
                i += 1
                if i >= n:
                    break
                if s[i] in avail:
                    avail.remove(s[i])
                cnt[s[i]] += 1
            i += 1
        return ans

sol = Solution()
print(sol.maxPartitionsAfterOperations("accca", 2)) # 3
print(sol.maxPartitionsAfterOperations("aabaab", 3)) # 1
print(sol.maxPartitionsAfterOperations("xxyz", 1)) # 4
print(sol.maxPartitionsAfterOperations("abb", 1)) # 3
print(sol.maxPartitionsAfterOperations("foukwieyawfmtlammvxpinpqtpyrzqhhqtlgxxpcbxhej", 5)) # 9