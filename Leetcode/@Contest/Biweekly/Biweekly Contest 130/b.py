import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        pos = defaultdict(list)
        for tag, (x, y) in zip(s, points):
            pos[tag].append((x, y))

        def check(k): # 檢查是否有兩個同樣標籤的點在距離 k 內
            for tag in pos:
                if len(pos[tag]) <= 1:
                    continue
                cnt = 0
                for x, y in pos[tag]:
                    if abs(x) <= k and abs(y) <= k:
                        cnt += 1
                        if cnt >= 2:
                            return True
            return False
        left, right = 0, int(1e9)
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        # print(right)
        ans = 0
        for tag in pos:
            for x, y in pos[tag]:
                if abs(x) <= right and abs(y) <= right:
                    ans += 1
                    break
        return ans
    
sol = Solution()
print(sol.maxPointsInsideSquare([[2,2],[-1,-2],[-4,4],[-3,1],[3,-3]], "abdca")) # 2
print(sol.maxPointsInsideSquare([[1,1],[-2,-2],[-2,2]], "abb")) # 1
print(sol.maxPointsInsideSquare([[1,1],[-1,-1],[2,-2]], "ccd")) # 0
print(sol.maxPointsInsideSquare([[-1,-4],[16,-8],[13,-3],[-12,0]], "abda")) # 1