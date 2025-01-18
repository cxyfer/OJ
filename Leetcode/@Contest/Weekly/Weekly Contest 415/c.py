import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        prefixes = set()
        for word in words:
            for i in range(1, len(word) + 1):
                prefixes.add(word[:i])
        
        n = len(target)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0  # 空字串需要0個前綴
        
        for i in range(n):
            if dp[i] != float('inf'):
                for prefix in prefixes:
                    end = i + len(prefix)
                    if end > n:
                        continue
                    if target[i:end] == prefix:
                        if dp[end] > dp[i] + 1:
                            dp[end] = dp[i] + 1
                            
        return dp[n] if dp[n] != float('inf') else -1