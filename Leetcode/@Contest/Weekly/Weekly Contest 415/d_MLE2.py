import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

class TrieNode:
    def __init__(self):
        self.child = [None] * 26
        self.is_end = False
        self.fail = None
        self.outputs = []

class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        n = len(target)

        root = TrieNode()
        for word in words:
            node = root
            for idx, ch in enumerate(word):
                if node.child[ord(ch) - ord('a')] is None:
                    node.child[ord(ch) - ord('a')] = TrieNode()
                node = node.child[ord(ch) - ord('a')]
                node.outputs.append(idx + 1) # Store the length of the prefix
            node.is_end = True

        # Build the fail links
        q = deque()
        for child in root.child:
            if child is not None:
                child.fail = root
                q.append(child)

        while q:
            node = q.popleft()
            for ch, child in enumerate(node.child):
                if child is None:
                    continue
                fail_node = node.fail
                while fail_node and fail_node.child[ch] is None:
                    fail_node = fail_node.fail
                child.fail = fail_node.child[ch] if fail_node and fail_node.child[ch] is not None else root
                child.outputs += child.fail.outputs if child.fail else []
                q.append(child)


        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        node = root

        for i in range(n):
            ch = ord(target[i]) - ord('a')
            while node and node.child[ch] is None:
                node = node.fail
            node = node.child[ch] if node and node.child[ch] is not None else root

            temp_node = node
            while temp_node:
                for length in temp_node.outputs:
                    start_pos = i + 1 - length
                    if dp[start_pos] != float('inf'):
                        dp[i + 1] = min(dp[i + 1], dp[start_pos] + 1)
                temp_node = temp_node.fail

        return dp[n] if dp[n] != float('inf') else -1