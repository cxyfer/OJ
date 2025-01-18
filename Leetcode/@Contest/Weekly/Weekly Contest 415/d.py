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
        self.fail = None
        self.is_end = False
        self.depth = 0
        self.dict_suffix = None

class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        n = len(target)

        root = TrieNode()
        for word in words:
            node = root
            for ch in word:
                if ch not in node.child:
                    child_node = TrieNode()
                    child_node.depth = node.depth + 1
                    node.child[ch] = child_node
                node = node.child[ch]
                node.is_end = True

        q = deque()
        for child in root.child.values():
            child.fail = root
            child.dict_suffix = child if child.is_end else None
            q.append(child)

        while q:
            node = q.popleft()
            for ch, child in node.child.items():
                fail_node = node.fail
                while fail_node != root and ch not in fail_node.child:
                    fail_node = fail_node.fail
                child.fail = fail_node.child.get(ch, root) if ch in fail_node.child else root
                child.dict_suffix = child if child.is_end else child.fail.dict_suffix
                q.append(child)

        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        node = root
        for i in range(n):
            ch = target[i]
            while node != root and ch not in node.child:
                node = node.fail
            node = node.child.get(ch, root)
            temp_node = node
            while temp_node:
                if temp_node.is_end:
                    length = temp_node.depth
                    start_pos = i + 1 - length
                    if dp[start_pos] != float('inf'):
                        dp[i + 1] = min(dp[i + 1], dp[start_pos] + 1)
                temp_node = temp_node.dict_suffix
        return dp[n] if dp[n] != float('inf') else -1
