import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        def check(red, blue):
            res = 0
            while red > res or blue > res:
                res += 1
                if res & 1:
                    if red >= res:
                        red -= res
                    else:
                        return res - 1  
                else:
                    if blue >= res:
                        blue -= res
                    else:
                        return res - 1
            return res
        # print(check(red, blue), check(blue, red))
        return max(check(red, blue), check(blue, red))
    


sol = Solution()
print(sol.maxHeightOfTriangle(2, 4)) # 3
print(sol.maxHeightOfTriangle(2, 1)) # 2
print(sol.maxHeightOfTriangle(1, 1)) # 1
print(sol.maxHeightOfTriangle(10, 1)) # 2
print(sol.maxHeightOfTriangle(10, 10)) # 5
print(sol.maxHeightOfTriangle(9, 3)) # 3