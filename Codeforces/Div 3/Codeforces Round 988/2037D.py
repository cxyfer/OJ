import heapq
from heapq import heappop, heappush

t = int(input())

for _ in range(t):
    n, m, L = map(int, input().split())
    obstacles = [tuple(map(int, input().split())) for _ in range(n)]
    powerups = [tuple(map(int, input().split())) for _ in range(m)]

    # Merge intervals
    obstacles.sort(key = lambda x: x[0])
    intervals = []
    for l, r in obstacles:
        if intervals and intervals[-1][1] >= l:
            intervals[-1][1] = max(intervals[-1][1], r)
        else:
            intervals.append((l, r))
    obstacles = intervals
    powerups.sort(key = lambda x: x[0])

    ans = 0
    cur = 1
    hp = []
    i = 0
    for l, r in obstacles:
        while i < m and powerups[i][0] < l:
            x, v = powerups[i]
            heappush(hp, -v)
            i += 1
        while hp and r - l + 2 > cur:
            cur += -heappop(hp)
            ans += 1
        if r - l + 2 > cur:
            ans = -1
            break

    print(ans)