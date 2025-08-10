"""
y = mx + k
m = dy / dx
k = y1 - m*x1 = (y1x2 - y1x1 - x1y2  + x1y1) / dx = (y1x2 - x1y2) / dx

相比 3625. Count Number of Trapezoids II，
這題因為題目保證不會有三點共線，所以不需要考慮共線的情況，可以省略很多計算。
"""
from collections import defaultdict
from math import gcd

N = int(input())
points = [list(map(int, input().split())) for _ in range(N)]

def get_line(x1: int, y1: int, x2: int, y2: int):
    dx = x2 - x1
    dy = y2 - y1
    k = y1 * x2 - x1 * y2
    g = gcd(dx, dy, k)
    dx //= g
    dy //= g
    k //= g
    if dx < 0 or dx == 0 and dy < 0:
        dx, dy, k = -dx, -dy, -k
    return (dx, dy), k

# cnt1[m] 為斜率為 m 的直線數量
cnt1 = defaultdict(int)
# cnt2[(x, y)] 為中點為 (x // 2, y // 2) 的直線數量
cnt2 = defaultdict(int)
for i, (x1, y1) in enumerate(points):
    for j in range(i + 1, N):
        x2, y2 = points[j]
        m, k = get_line(x1, y1, x2, y2)
        cnt1[m] += 1
        cnt2[(x1 + x2, y1 + y2)] += 1

ans = 0
# 和相同斜率的其他直線可以構成梯形
for m, v in cnt1.items():
    ans += v * (v - 1) // 2

# 減去平行四邊形數量
for v in cnt2.values():
    ans -= v * (v - 1) // 2

print(ans)