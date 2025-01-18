import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

class TrieNode:
    def __init__(self):
        self.child = {}
        self.is_end = False

class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        n = len(target)

        root = TrieNode()
        for word in words:
            node = root
            for ch in word:
                if ch not in node.child:
                    node.child[ch] = TrieNode()
                node = node.child[ch]
            node.is_end = True

        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(n):
            if dp[i] == float('inf'):
                continue
            node = root
            j = i
            while j < n and target[j] in node.child:
                node = node.child[target[j]]
                j += 1
                dp[j] = min(dp[j], dp[i] + 1)
                
        return dp[n] if dp[n] != float('inf') else -1