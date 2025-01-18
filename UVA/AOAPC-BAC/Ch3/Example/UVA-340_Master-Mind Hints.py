"""
    Counter
    tags: Counter, Simulation, 紫書-Ch3, CPE-240424
"""
from collections import Counter
tc = 1
while True:
    n = int(input())
    if n == 0:
        break
    print(f"Game {tc}:")
    tc += 1
    s = list(map(int, input().split()))
    while True:
        g = list(map(int, input().split())) # guess
        if all(x == 0 for x in g):
            break
        A, B = 0, 0
        cnt_s = Counter(s)
        cnt_g = Counter(g)
        for i in range(n):
            if s[i] == g[i]:
                A += 1
                cnt_s[s[i]] -= 1
                cnt_g[g[i]] -= 1
        for k in cnt_g:
            B += min(cnt_s[k], cnt_g[k])
        print(f"    ({A},{B})")