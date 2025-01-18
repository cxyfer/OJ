from functools import cache

import sys
input = sys.stdin.readline
def print(val=""): sys.stdout.write(str(val)+"\n")

t = int(input())
for _ in range(t):
    s = input().strip()
    n = len(s)

    @cache
    def dfs(i): # 以第 s[i] 結尾的最大和
        if i < 0:
            return 0
        res = 0
        cur, p = 0, 1
        for st in range(i, -1, -1):
            cur += int(s[st]) * p
            p *= 10
            if s[st] == '0' and i - st + 1 > 1:
                continue
            # cur = int(s[st:i+1])
            if cur > (1 << 31) - 1: # Pruning
                break
            res = max(res, dfs(st-1) + cur)
        return res
    print(dfs(n-1))