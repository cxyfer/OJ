import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

# 維護區間內有多少組相鄰字元是相同的 ?

# FenwickTree Template
class BIT:  # PURQ, 1-based
    __slots__ = ['tree']

    def __init__(self, n: int):
        self.tree = [0] * (n + 1)

    def add(self, k: int, x: int) -> None:  # 令 nums[k] += x
        while k < len(self.tree):
            self.tree[k] += x
            k += k & -k

    def preSum(self, k: int) -> int:  # 求 nums[:k+1] 之和
        res = 0
        while k > 0:
            res += self.tree[k]
            k -= (k & -k)
        return res

    def query(self, l: int, r: int) -> int:  # 求 nums[l:r+1] 之和
        if l > r:
            return 0
        return self.preSum(r) - self.preSum(l - 1)
        
class Solution:
    def minDeletions(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        A = list(map(lambda c: ord(c) - ord('A'), s))
 
        bit = BIT(n)
        for i, (x, y) in enumerate(pairwise(A), 1):
            if x == y:
                bit.add(i, 1)
                
        ans = []
        for op, *args in queries:
            if op == 1:
                idx = args[0]
                if idx > 0:
                    bit.add(idx, -1 if A[idx - 1] == A[idx] else 1)
                if idx < n - 1:
                    bit.add(idx + 1, -1 if A[idx] == A[idx + 1] else 1)
                A[idx] ^= 1
            else:
                l, r = args[0], args[1]
                ans.append(bit.query(l + 1, r) if l < r else 0)
        return ans

sol = Solution()
print(sol.minDeletions("ABA", [[2,1,2],[1,1],[2,0,2]]))  #[0,2]
print(sol.minDeletions("BAAB", [[2,2,2],[1,2],[1,1],[2,1,3]]))  #[0,2]