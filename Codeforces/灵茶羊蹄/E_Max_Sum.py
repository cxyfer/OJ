from heapq import *

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    pairs = [(a, b) for a, b in zip(A, B)]
    pairs.sort(key = lambda x : x[0])
    
    ans = float("inf")
    hp = []
    s = 0
    for a, b in pairs:
        heappush(hp, -b)
        s += b
        if len(hp) < k:
            continue
        if len(hp) > k:
            v = -heappop(hp)
            s -= v
        ans = min(ans, a * s)
    print(ans)