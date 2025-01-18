import math

t = int(input())

for _ in range(t):
    k, l1, r1, l2, r2 = map(int, input().split())

    ans = 0
    kn = 1
    while kn <= r2:
        lo = max(l1, math.ceil(l2 / kn))
        hi = min(r1, math.floor(r2 / kn))
        ans += max(hi - lo + 1, 0)
        kn *= k
    print(ans)