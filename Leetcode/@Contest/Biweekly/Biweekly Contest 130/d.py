import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *


"""

0000
0001
0010
0011

f(i) = 2 * f(i-1) + 2^i


"""
calc = [1] * 50 # < 2^(i+1) 的數字裡面有幾個 1
for i in range(1, 50):
    calc[i] = 2 * calc[i - 1] + pow(2, i)
class Solution:
    def findProductsOfElements(self, queries: List[List[int]]) -> List[int]:
        big_nums = []
        for x in range(1, 100):
            cur = []
            while x:
                cur.append(x & -x)
                x -= x & -x
            big_nums.extend(cur)
        print(len(big_nums))
        ans = []
        for l, r, m in queries:
            prod = 1
            for i in range(l, r + 1):
                prod = prod * big_nums[i] % m
            ans.append(prod)
        return ans
                
    
sol = Solution()
print(sol.findProductsOfElements([[1,3,7]])) # [4]
print(sol.findProductsOfElements([[2,5,3],[7,7,4]])) # [2, 2]