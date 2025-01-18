import math
import itertools

N, S, T = map(int, input().split())
segments = [tuple(map(int, input().split())) for _ in range(N)]

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

ans = float('inf')

for order in itertools.permutations(range(N)):
    for flags in itertools.product([0, 1], repeat=N):
        tot = 0
        cur = (0, 0)
        for i, seg_index in enumerate(order):
            flag = flags[i]
            seg = segments[seg_index]
            
            if flag == 0:
                st, ed = (seg[0], seg[1]), (seg[2], seg[3])
            else:
                st, ed = (seg[2], seg[3]), (seg[0], seg[1])
            
            tot += distance(cur[0], cur[1], st[0], st[1]) / S
            tot += distance(st[0], st[1], ed[0], ed[1]) / T
            cur = ed
        ans = min(ans, tot)
print(f"{ans:.20f}")
