import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        def check(T: int) -> bool:
            cnt = 0
            for time in workerTimes:
                if time == 0:
                    continue
                discriminant = 1 + 8 * T // time
                if discriminant < 0:
                    continue
                sqrt_discriminant = math.isqrt(discriminant)
                x = (sqrt_discriminant - 1) // 2
                if x > 0:
                    cnt += x
                if cnt >= mountainHeight:
                    return True
            return cnt >= mountainHeight

        left, right = 0, max(workerTimes) * mountainHeight * \
            (mountainHeight + 1) // 2

        ans = right
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
# 建立 Solution 的實例
solution = Solution()

# 範例 1
mountainHeight1 = 4
workerTimes1 = [2,1,1]
print(solution.minNumberOfSeconds(mountainHeight1, workerTimes1))  # 輸出: 3

# 範例 2
mountainHeight2 = 10
workerTimes2 = [3,2,2,4]
print(solution.minNumberOfSeconds(mountainHeight2, workerTimes2))  # 輸出: 12

# 範例 3
mountainHeight3 = 5
workerTimes3 = [1]
print(solution.minNumberOfSeconds(mountainHeight3, workerTimes3))  # 輸出: 15
