import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *
from random import *

"""
Q4. ||Binary Search + Rolling Hash||
||對於要比對有沒有重複子陣列(字串)的問題，直覺想到 Rolling Hash，但顯然逐長度檢查會超時。
注意到當存在為 ln 的子陣列滿足條件時，在該子陣列延伸一個元素也一定滿足條件，
因此具有單調性，可以使用 Binary Search 來解決。||
||O(n log n)||

fun fact: 因為測試時為了驗證滑動窗口沒有寫錯，把對雜湊值取模先刪了，結果後面忘了加回來，導致被硬控了30+分鐘。
"""

MOD = 1070777777
BASE = randint(int(1e8), int(1e9))


class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        P = [1] + [0] * n
        for i in range(n):
            P[i + 1] = P[i] * BASE % MOD

        def check(mid: int) -> bool:
            hs = 0
            cnt = defaultdict(int)
            for right, x in enumerate(nums):
                hs = hs * BASE + x
                hs %= MOD
                if right + 1 >= mid:
                    cnt[hs] += 1
                    hs -= nums[right + 1 - mid] * P[mid - 1]
                    hs %= MOD
            return any(v == 1 for v in cnt.values())

        left, right = 1, n - 1
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left


sol = Solution()
print(sol.smallestUniqueSubarray([839, 12763, 839, 12763, 839, 12763]))  # 4
print(sol.smallestUniqueSubarray([1, 2, 1, 2, 1, 2]))  # 4
print(sol.smallestUniqueSubarray([1, 2, 1, 2, 1, 2, 1, 2]))  # 6
