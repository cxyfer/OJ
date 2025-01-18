import math
from typing import *
from collections import *
from functools import lru_cache, cache
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        not_used = set(nums)
        cnt = Counter(nums)
        for k in sorted(cnt.keys()): # 讓數字盡可能的變多且保留原本的數字，把重複的數字往後推(加一)
            v = cnt[k]
            if v > 1:
                if k in not_used:
                    not_used.remove(k)
                cnt[k+1] += v - 1
                cnt[k] = 1
        not_used = sorted(not_used)

        @cache # Memoization
        def solve1(k): # 從 k 開始最長的連續數字長度
            if k not in cnt.keys():
                return 0
            return 1 + solve1(k+1)
        
        ans = 1
        for k in sorted(cnt.keys()): # 從每個數字開始找最長的連續數字
            ans = max(ans, solve1(k))
        
        # 分組循環，在未使用的數字中找連續的數字
        lst = []
        i = 0
        while i < len(not_used):
            j = i
            while j < len(not_used) and not_used[j] == not_used[i] + (j - i):
                j += 1
            lst.append(not_used[i:j])
            i = j
        # 對於每組連續的數字 x ，都使其往後推(加一)，考慮在原本的數字中找從 x[-1] + 2 開始的最長連續數字
        # 舉例來說，若連續數字為 [4,5,6] ，則加一後為 [5,6,7] ，在原本的數字中找從 8 開始的最長連續數字
        for x in lst:
            ans = max(ans, len(x) + solve1(x[-1] + 2))
        return ans
sol = Solution()

print(sol.maxSelectedElements([2,1,5,1,1])) # 3
print(sol.maxSelectedElements([1,4,7,10])) # 1
print(sol.maxSelectedElements([8,10,6,12,9,12,2,3,13,19,11,18,10,16])) # 8
print(sol.maxSelectedElements([12,11,8,7,2,10,18,12])) # 6