import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        n = len(nums)

        if k > n // 2:
            return -1

        A = [max(max(nums[(i - 1) % n], nums[(i + 1) % n]) + 1 - nums[i], 0) for i in range(n)]

        def f(arr: list[int], k: int) -> int:
            n = len(arr)
            @cache
            def dfs(i: int, j: int) -> int:
                if j == 0:
                    return 0
                # if i >= n:  # MLE
                if i >= n or j > (n - i + 1) // 2:
                    return float('inf')
                return min(arr[i] + dfs(i + 2, j - 1), dfs(i + 1, j))
            ans = dfs(0, k)
            dfs.cache_clear()
            return ans
        return min(f(A[1:], k), A[0] + f(A[2:n-1], k - 1))


sol = Solution()
print(sol.minOperations([2,1,2], 1)) # 1
print(sol.minOperations([4,5,3,6], 2)) # 0