import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

class Node: # Trie
    def __init__(self):
        self.child = [None] * 26
        self.isEnd = False
        self.cost = float("inf")

class Solution:
    def minimumCost(self, target: str, words: List[str], costs: List[int]) -> int:
        n = len(target)

        trie = Node() # 反向
        for word, cost in zip(words, costs):
            node = trie
            for c in reversed(word):
                idx = ord(c) - ord("a")
                if node.child[idx] is None:
                    node.child[idx] = Node() # type: ignore
                node = node.child[idx]
            node.isEnd = True
            # node.cost = min(node.cost, cost)
            if cost < node.cost:
                node.cost = cost
            
        dp = [float("inf")] * (n + 1)

        dp[0] = 0
        for i in range(1, n + 1):
            cur = trie
            for j in range(i - 1, -1, -1):
                idx = ord(target[j]) - ord("a")
                if cur.child[idx] is None:
                    break
                cur = cur.child[idx]
                if cur.isEnd:
                    # dp[i] = min(dp[i], dp[j] + cur.cost)
                    if dp[j] + cur.cost < dp[i]:
                        dp[i] = dp[j] + cur.cost
        return dp[n] if dp[n] != float("inf") else -1
        

with open("data.in", "w") as f:
    f.write(f"\"{'a' * 50000}\"")
    f.write("\n")
    f.write("[")
    for i in range(5):
        f.write(f"\"{'a' * 50000}\",")
    f.write("]")
    f.write("\n")
    f.write("[")
    for i in range(5):
        f.write(f"100,")
    f.write("]")
    f.write("\n")

sol = Solution()
print(sol.minimumCost("abcdef", ["abdef","abc","d","def","ef"], [100,1,1,10,5])) # 7
print(sol.minimumCost("aaaa", ["z","zz","zzz"], [1,10,100])) # -1
print(sol.minimumCost("r", ["r","r","r","r"], [1,10,100,1000])) # 1