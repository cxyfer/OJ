import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *


class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        n = len(word)
        vowels = set('aeiou')
        ans = 0

        for i in range(n):
            cur = set()  # set of vowels
            cnt = 0  # count of consonants
            for j in range(i, n):
                ch = word[j]
                if ch in vowels:
                    cur.add(ch)
                else:
                    cnt += 1
                if len(cur) == 5 and cnt == k:
                    ans += 1
        return ans

# iqeaouqi

# def count_substrings_with_vowels_and_k_consonants(word: str, k: int) -> int:


sol = Solution()
print(sol.countOfSubstrings("aeioqq", 1)) # 0
print(sol.countOfSubstrings("aeiou", 0)) # 1
print(sol.countOfSubstrings("ieaouqqieaouqq", 1)) # 3
print(sol.countOfSubstrings("iqeaouqi", 2)) # 3

# 0 6 iqeaouq
# 0 7 iqeaouqi
# 1 7 qeaouqi
# 0 6 iqeaouq
# 0 7 iqeaouqi