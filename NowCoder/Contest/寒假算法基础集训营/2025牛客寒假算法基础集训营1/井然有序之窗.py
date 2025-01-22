from heapq import *

n = int(input())

intervals = []
for idx in range(n):
    l, r = map(int, input().split())
    intervals.append((l, r, idx))
intervals.sort(key=lambda x: x[0])

ans = [0] * n
hp = []
i = 0
for x in range(1, n+1):
    while i < n and intervals[i][0] <= x:
        l, r, idx = intervals[i]
        heappush(hp, (r, idx))
        i += 1

    if not hp:
        exit(print(-1))

    r, idx = heappop(hp)
    if r < x:
        exit(print(-1))
    ans[idx] = x

print(*ans)