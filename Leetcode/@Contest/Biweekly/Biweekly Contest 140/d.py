import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

import numpy as np
from random import randint

class Solution:
    def minStartingIndex(self, s: str, pattern: str) -> int:
        n, m = len(s), len(pattern)

        BASE1 = randint(int(8e8), int(9e8))
        MOD1 = 10**9 + 7

        BASE2 = randint(int(8e8), int(9e8))
        MOD2 = 10**9 + 9

        power1 = [1] * (m + 1)
        power2 = [1] * (m + 1)
        for i in range(1, m + 1):
            power1[i] = (power1[i - 1] * BASE1) % MOD1
            power2[i] = (power2[i - 1] * BASE2) % MOD2

        hash_p1  = 0
        hash_p2  = 0
        for i, ch in enumerate(pattern):
            hash_p1 = (hash_p1 + (ord(ch) - ord('a') + 1) * power1[i]) % MOD1
            hash_p2 = (hash_p2 + (ord(ch) - ord('a') + 1) * power2[i]) % MOD2
        
        st = set()
        st.add((hash_p1, hash_p2))
        for i, ch in enumerate(pattern):
            cur = ord(ch) - ord('a')
            for c2 in range(26):
                if c2 == cur:
                    continue
                new_char_val = c2 + 1
                hash_new1 = (hash_p1 - (cur +1) * power1[i] + new_char_val * power1[i]) % MOD1
                hash_new2 = (hash_p2 - (cur +1) * power2[i] + new_char_val * power2[i]) % MOD2
                st.add((hash_new1, hash_new2))

        hash_s1 = 0
        hash_s2 = 0
        for i in range(m):
            hash_s1 = (hash_s1 + (ord(s[i]) - ord('a') +1) * power1[i]) % MOD1
            hash_s2 = (hash_s2 + (ord(s[i]) - ord('a') +1) * power2[i]) % MOD2

        if (hash_s1, hash_s2) in st:
            return 0

        base1_inv = pow(BASE1, MOD1 - 2, MOD1)
        base2_inv = pow(BASE2, MOD2 - 2, MOD2)

        for k in range(1, n - m +1):
            lc_val = ord(s[k -1]) - ord('a') +1
            hash_s1 = (hash_s1 - lc_val) % MOD1
            hash_s2 = (hash_s2 - lc_val) % MOD2

            hash_s1 = (hash_s1 * base1_inv) % MOD1
            hash_s2 = (hash_s2 * base2_inv) % MOD2

            rc_val = ord(s[k + m -1]) - ord('a') +1
            hash_s1 = (hash_s1 + rc_val * power1[m -1]) % MOD1
            hash_s2 = (hash_s2 + rc_val * power2[m -1]) % MOD2

            if (hash_s1, hash_s2) in st:
                return k
            
        return -1
# 測試案例
solution = Solution()

# 範例 1
s1 = "abcdefg"
pattern1 = "bcdffg"
print(solution.minStartingIndex(s1, pattern1))  # 輸出: 1

# 範例 2
s2 = "ababbababa"
pattern2 = "bacaba"
print(solution.minStartingIndex(s2, pattern2))  # 輸出: 4

# 範例 3
s3 = "abcd"
pattern3 = "dba"
print(solution.minStartingIndex(s3, pattern3))  # 輸出: -1

# 範例 4
s4 = "dde"
pattern4 = "d"
print(solution.minStartingIndex(s4, pattern4))  # 輸出: 0
