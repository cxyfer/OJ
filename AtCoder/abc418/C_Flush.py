from itertools import *
from bisect import *

N, Q = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
s = list(accumulate(A, initial=0))
for _ in range(Q):
    b = int(input())
    if b > A[-1]:
        print(-1)
        continue
    idx = bisect_left(A, b)
    ans = s[idx] + (N - idx) * (b - 1) + 1
    print(ans)