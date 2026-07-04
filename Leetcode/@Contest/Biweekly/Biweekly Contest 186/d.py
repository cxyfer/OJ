import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

"""

## Q4. DP
定義 dfs(i, j, k) 表示從 word1[i:] 和 word2[j:] 開始選字元，匹配整個 target[k:] 的方案數。
則直接枚舉 i' >= i 和 j' >= j 檢查是否可以選 i' 或 j' 來匹配 target[k] 即可。
遞迴入口為 dfs(0, 0, 0)

由於三個字串長度最大為 1e2，因此總狀態數量為 1e6，且每個狀態最多枚舉 2e2 次，因此總時間複雜度為 O(n^4)，應該可以接受。
"""

MOD = int(1e9) + 7


class Solution:
    def interleaveCharacters(self, word1: str, word2: str, target: str) -> int:
        n1, n2, m = len(word1), len(word2), len(target)

        @cache
        def dfs(i: int, j: int, k: int) -> int:
            if k == m:
                return 1 if i > 0 and j > 0 else 0
            if i == n1 and j == n2:
                return 0
            res = 0
            for ni in range(i, n1):
                if word1[ni] == target[k]:
                    res += dfs(ni + 1, j, k + 1)
            for nj in range(j, n2):
                if word2[nj] == target[k]:
                    res += dfs(i, nj + 1, k + 1)
            return res % MOD

        return dfs(0, 0, 0)


sol = Solution()
print(sol.interleaveCharacters("abc", "bac", "abc"))  # 5
print(sol.interleaveCharacters("cd", "cd", "ccd"))  # 4
print(sol.interleaveCharacters("xy", "xy", "xyxy"))  # 2
print(sol.interleaveCharacters("ab", "cde", "ace"))  # 1
print(sol.interleaveCharacters("h", "jgjgj", "jh"))  # 3
