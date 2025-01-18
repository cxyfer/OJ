import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def kthCharacter(self, k: int) -> str:
        s = "a"
        while len(s) < k:
            s += ''.join([chr(((ord(ch) - ord('a') + 1) % 26) + ord('a')) for ch in s])
        return s[k-1]

# 測試範例
sol = Solution()
print(sol.kthCharacter(5))   # 輸出: "b"
print(sol.kthCharacter(10))  # 輸出: "c"
