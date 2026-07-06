import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from string import *

MX_N = (int(1e4) + 5) // 2
fact = [1] * MX_N
for i in range(2, MX_N):
    fact[i] = fact[i-1] * i

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        n = len(s)
        cnt = Counter(s)
        mid = ''
        for ch, val in cnt.items():
            if val % 2 != 0:
                mid = ch
            cnt[ch] = val // 2

        candidates = []
        for ch, val in sorted(cnt.items()):
            candidates.extend([ch] * val)
        
        m = len(candidates)
        if m == 0:
            return mid if k == 1 else ""

        tot = fact[m]
        for val in cnt.values():
            tot //= fact[val]

        if tot < k:
            return ""

        ans = ''
        for _ in range(m):
            for ch in ascii_lowercase:
                if cnt[ch] == 0:
                    continue

                tot *= fact[cnt[ch]]
                tot //= m
                cnt[ch] -= 1
                m -= 1
                tot //= fact[cnt[ch]]
                if k <= tot:
                    ans += ch
                    break 
                else:
                    k -= tot
                    tot *= fact[cnt[ch]]
                    cnt[ch] += 1
                    m += 1
                    tot *= m
                    tot //= fact[cnt[ch]]

        return ans + mid + ans[::-1]

sol = Solution()
print(sol.smallestPalindrome("abba", 2))  # baab
print(sol.smallestPalindrome("aa", 2))  # ""
print(sol.smallestPalindrome("bacab", 1))  # abcba
print(sol.smallestPalindrome("kkkk", 1))  # kkkk
print(sol.smallestPalindrome("aaaabbbbbbaaaa", 34))  # bbabaaaaaababb
