"""
D. 小L的扩展
https://ac.nowcoder.com/acm/contest/120566/D

Dijkstra 模板題
只需要另外維護一個 avail 陣列，表示該位置最早可以被訪問的時間即可。
Python 用二維陣列會 TLE，拉平成一維陣列即可。
"""

from heapq import heappush, heappop

# fmt: off
import sys
it = iter(sys.stdin.read().splitlines())
def input():
    return next(it)
# fmt: on


def solve():
    n, m, a, b = map(int, input().split())

    tot = n * m
    dist = [float("inf")] * tot
    avail = [float("-inf")] * tot

    hp = []
    for _ in range(a):
        r, c = map(lambda x: int(x) - 1, input().split())
        u = r * m + c
        dist[u] = 0
        heappush(hp, (0, u))

    for _ in range(b):
        r, c, t = map(int, input().split())
        r, c = r - 1, c - 1
        avail[r * m + c] = t

    while hp:
        d, u = heappop(hp)
        r, c = u // m, u % m

        if d > dist[u]:
            continue

        for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
            if 0 <= nr < n and 0 <= nc < m:
                v = nr * m + nc
                nd = max(d + 1, avail[v])
                if nd < dist[v]:
                    dist[v] = nd
                    heappush(hp, (nd, v))

    print(d)


if __name__ == "__main__":
    solve()
