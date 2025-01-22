from collections import *
from math import *

n = int(input())
A = list(map(int, input().split()))

mx = max(A)
ans = 0
cnt = Counter(A)
for g in range(1, mx + 1):
    for x in range(g, mx + 1, g):
        y = x ^ g
        if gcd(x, y) == g:
            ans += cnt[x] * cnt[y]
print(ans // 2)