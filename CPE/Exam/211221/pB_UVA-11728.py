from math import isqrt

MAXN = 1005
ans = [-1] * MAXN # pre-calculate
ans[1] = 1
for x in range(2, MAXN): 
    cur = 1 + x
    for p in range(2, isqrt(x) + 1):
        if x % p == 0:
            if p * p == x: # x is a perfect square
                cur += p
            else:
                cur += p + x // p
    if cur < MAXN:
        ans[cur] = x


kase = 1
while True:
    n = int(input())
    if n == 0:
        break
    print(f"Case {kase}: {ans[n]}")
    kase += 1