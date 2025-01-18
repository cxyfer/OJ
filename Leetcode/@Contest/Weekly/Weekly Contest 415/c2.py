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
        
        @cache
        def dfs(i):
            if i == n:
                return 0
            node = root
            min_count = float('inf')
            for j in range(i, n):
                ch = target[j]
                if ch in node.child:
                    node = node.child[ch]
                    count = dfs(j + 1)
                    if count != -1:
                        min_count = min(min_count, count + 1)
                else:
                    break
            return -1 if min_count == float('inf') else min_count
        
        return dfs(0)
