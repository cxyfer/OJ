import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
import random
import sys

sys.setrecursionlimit(1 << 25)

class Solution:
    def findAnswer(self, parent: List[int], s: str) -> List[bool]:
        n = len(parent)
        tree = defaultdict(list)
        for i in range(1, n):
            tree[parent[i]].append(i)
        
        MOD1 = random.randint(int(1e9), int(1e10))
        MOD2 = random.randint(int(1e9), int(1e10))
        BASE = random.randint(27, 100)

        P1 = [1] * (n + 1) # power of BASE
        P2 = [1] * (n + 1)
        for i in range(1, n + 1):
            P1[i] = (P1[i-1] * BASE) % MOD1
            P2[i] = (P2[i-1] * BASE) % MOD2

        HF1 = [0] * n # forward hash
        HF2 = [0] * n
        HB1 = [0] * n # backward hash
        HB2 = [0] * n
        ln = [0] * n  # dfsStr length

        def dfs1(u):
            nonlocal tree, s, HF1, HF2, HB1, HB2, ln
            cur_ln = 0
            hf1, hf2, hb1, hb2 = 0, 0, 0, 0
            for child in sorted(tree[u]):
                dfs1(child)
                hf1 = (hf1 * P1[ln[child]] + HF1[child]) % MOD1
                hf2 = (hf2 * P2[ln[child]] + HF2[child]) % MOD2
                hb1 = (HB1[child] * P1[cur_ln] + hb1) % MOD1
                hb2 = (HB2[child] * P2[cur_ln] + hb2) % MOD2
                cur_ln += ln[child]
            ch = ord(s[u]) - ord('a') + 1
            hf1 = (hf1 * BASE + ch) % MOD1
            hf2 = (hf2 * BASE + ch) % MOD2
            hb1 = (ch * P1[cur_ln] + hb1) % MOD1
            hb2 = (ch * P2[cur_ln] + hb2) % MOD2
            cur_ln += 1
            HF1[u], HF2[u], HB1[u], HB2[u] = hf1, hf2, hb1, hb2
            ln[u] = cur_ln

        def dfs2(u):
            nonlocal tree, s, HF1, HF2, HB1, HB2, ln
            cur_ln = 0
            hf1, hf2, hb1, hb2 = 0, 0, 0, 0
            for child in tree[u]:
                dfs2(child)
                hf1 = (hf1 * P1[ln[child]] + HF1[child]) % MOD1
                hf2 = (hf2 * P2[ln[child]] + HF2[child]) % MOD2
                hb1 = (HB1[child] * P1[cur_ln] + hb1) % MOD1
                hb2 = (HB2[child] * P2[cur_ln] + hb2) % MOD2
                cur_ln += ln[child]
            ch = ord(s[u]) - ord('a') + 1
            hf1 = (hf1 * BASE + ch) % MOD1
            hf2 = (hf2 * BASE + ch) % MOD2
            hb1 = (ch * P1[cur_ln] + hb1) % MOD1
            hb2 = (ch * P2[cur_ln] + hb2) % MOD2
            cur_ln += 1
            HF1[u], HF2[u], HB1[u], HB2[u] = hf1, hf2, hb1, hb2
            ln[u] = cur_ln

        for u in range(n):
            if parent[u] == -1:
                dfs2(u)
        
        ans = [False] * n
        for u in range(n):
            if HF1[u] == HB1[u] and HF2[u] == HB2[u]:
                ans[u] = True
        return ans

sol = Solution()
print(sol.findAnswer([-1,0,0,1,1,2], "aababa")) # [True,True,False,True,True,True]
print(sol.findAnswer([-1,0,0,0,0], "aabcb")) # [True,True,True,True,True]