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
        self.failure = None
        self.outputs = []

class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:

        root = TrieNode()
        for word in words:
            node = root
            for idx, ch in enumerate(word):
                if ch not in node.child:
                    node.child[ch] = TrieNode()
                node = node.child[ch]
                node.outputs.append(idx + 1) # Store the length of the prefix
            node.is_end = True

        # Build the failure links
        q = deque()
        for child in root.child.values():
            child.failure = root
            q.append(child)

        while q:
            node = q.popleft()
            for ch, child in node.child.items():
                failure_node = node.failure
                while failure_node and ch not in failure_node.child:
                    failure_node = failure_node.failure
                child.failure = failure_node.child[ch] if failure_node else root
                child.outputs += child.failure.outputs if child.failure else []
                q.append(child)

        n = len(target)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        node = root

        for i in range(n):
            ch = target[i]
            while node and ch not in node.child:
                node = node.failure
            node = node.child[ch] if node else root

            temp_node = node
            while temp_node:
                for length in temp_node.outputs:
                    start_pos = i + 1 - length
                    if dp[start_pos] != float('inf'):
                        dp[i + 1] = min(dp[i + 1], dp[start_pos] + 1)
                temp_node = temp_node.failure

        return dp[n] if dp[n] != float('inf') else -1