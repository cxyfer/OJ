"""
    Counter
    Similar to LeetCode 299. Bulls and Cows
    tags: Counter, Simulation, AOAPC-BAC-Ch3, CPE-240424
"""
from collections import Counter
kase = 1
while True:
    n = int(input())
    if n == 0:
        break
    print(f"Game {kase}:")
    kase += 1
    s = list(map(int, input().split())) # secret
    cnt_s0 = Counter(s)
    while True:
        g = list(map(int, input().split())) # guess
        if all(x == 0 for x in g):
            break
        A = 0
        cnt_s = cnt_s0.copy()
        cnt_g = Counter(g)
        for i in range(n):
            if s[i] == g[i]:
                A += 1
                cnt_s[s[i]] -= 1
                cnt_g[g[i]] -= 1
        B = sum(min(cnt_s[k], cnt_g[k]) for k in cnt_g)
        print(f"    ({A},{B})")