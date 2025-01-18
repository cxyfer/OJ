import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        dp = [float('-inf')] * 4  

        for num in b:  
            for k in reversed(range(4)):  
                if k == 0:  
                    dp[0] = max(dp[0], a[0] * num)  
                else:  
                    if dp[k-1] != float('-inf'):  
                        dp[k] = max(dp[k], dp[k-1] + a[k] * num)  

        return dp[3]