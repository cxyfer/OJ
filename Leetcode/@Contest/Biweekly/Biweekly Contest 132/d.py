import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        if k == 0:
            cnt = Counter(nums)
            return max(cnt.values())
        dp = [0 for _ in range(k+1)]
        st = [set() for _ in range(k+1)]
        cnt = [defaultdict(int) for _ in range(k+1)]

        for x in nums:
            prev = 0
            for j in range(k+1):
                cur = max(prev + 1, cnt[j][x] + 1)
                if x in st[j]:
                    cur = max(cur, (dp[j]+1))
                prev, cnt[j][x] = dp[j], cur
                if dp[j] < cur:
                    dp[j] = cur
                    st[j].clear()
                if cur == dp[j]:
                    st[j].add(x)
        return dp[k]

sol = Solution()
print(sol.maximumLength([1,2,1,1,3], 2)) # 4
print(sol.maximumLength([1,2,3,4,5,1], 0)) # 2
print(sol.maximumLength([59,60,59,60,60,60], 0)) # 4
print(sol.maximumLength([68,69,68,69,69,68,68], 1)) # 5
