import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)

        cnt = defaultdict(int)
        for x in nums:
            cnt[x % k] += 1
        ans = max(cnt.values())

        # 考慮前 i 個數字，且最後一個數字除以 k 的餘數為 j 的最大長度
        # 任兩數之和除以 k 的餘數為 target
        def check(target):
            dp = [0] * (k)
            dp[nums[0] % k] = 1
            for x in nums[1:]:
                x %= k
                y = (target - x + k) % k
                dp[x] = max(dp[x], dp[y] + 1)
            return max(dp)

        res2 = max(check(z) for z in range(k))
        return max(ans, res2)       

        # dp = [[0] * k for _ in range(n + 1)] 
        # dp[1][nums[0] % k] = 1
        # for i, x in enumerate(nums[1:], 2):
        #     x %= k
        #     for s in range(k): # 任兩數相加後除以 k 的餘數為 s
        #         y = (s - x + k) % k
        #         dp[i][j] = max(dp[i - 1][j], dp[i - 1][y] + 1)
        # print(ans)
        # print([x % k for x in nums])
        # print(dp)
        return max(ans, max(dp[-1]))


sol = Solution()
print(sol.maximumLength([1,2,3,4,5], 2)) # 5
print(sol.maximumLength([1,4,2,3,1,4], 3)) # 4

print(sol.maximumLength([2,10], 7)) # 2