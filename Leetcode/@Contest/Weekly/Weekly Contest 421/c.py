import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

from typing import List
from math import gcd
from collections import Counter

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10**9 + 7

        # f[g1][g2] 表示兩個子序列的 gcd 分別為 g1 和 g2 的方案數
        f = [[0] * 201 for _ in range(201)] 
        f[0][0] = 1
        
        for x in nums:
            new_f = [[0] * 201 for _ in range(201)]
            for g1 in range(201):
                for g2 in range(201):
                    val = f[g1][g2]
                    if val == 0:
                        continue
                    # 不選擇 x 作為子序列 A 和 B 的元素
                    new_f[g1][g2] = (new_f[g1][g2] + val) % MOD

                    # 選擇 x 作為子序列 A 的元素
                    new_g1 = x if g1 == 0 else gcd(g1, x)
                    new_f[new_g1][g2] = (new_f[new_g1][g2] + val) % MOD
  
                    # 選擇 x 作為子序列 B 的元素
                    new_g2 = x if g2 == 0 else gcd(g2, x)
                    new_f[g1][new_g2] = (new_f[g1][new_g2] + val) % MOD
            f = new_f
        
        return sum(f[g][g] for g in range(1, 201)) % MOD



sol = Solution()
print(sol.subsequencePairCount([1,2,3,4])) # 10
print(sol.subsequencePairCount([10,20,30])) # 2