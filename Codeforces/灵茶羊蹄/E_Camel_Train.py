from heapq import heappush, heappop
from collections import defaultdict

t = int(input())

for _ in range(t):
    n = int(input())
    A = defaultdict(list)
    B = defaultdict(list)   
    ans = 0
    for _ in range(n):
        k, l, r = map(int, input().split())
        if l > r:
            ans += r
            A[k].append(l - r)
        else:
            ans += l
            B[k].append(r - l)
    hp = []
    for k, ds in sorted(A.items()):
        for d in ds:
            heappush(hp, d)
            ans += d
            if len(hp) > k:
                ans -= heappop(hp)
    hp = []
    for k, ds in sorted(B.items(), reverse=True):
        for d in ds:
            heappush(hp, d)
            ans += d
            if len(hp) > n - k:
                ans -= heappop(hp)
    print(ans)