"""
U262369 选择最佳线路
https://www.luogu.com.cn/problem/U262369
https://www.luogu.com.cn/problem/T441226

本質上還是單源最短路問題，只是有多個起點。
可以新增一個虛擬源點，將虛擬源點連向所有起點，邊權為 0。
或是直接將所有起點放入優先隊列中，初始化距離為 0。
"""

from heapq import heappush, heappop

# fmt: off
import sys
it = iter(map(int, sys.stdin.buffer.read().split()))
def nxt():
    return next(it)
def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)) + end)
# fmt: on


def solve():
    n, m, ed = nxt(), nxt(), nxt()
    ed -= 1

    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v, w = nxt(), nxt(), nxt()
        u, v = u - 1, v - 1
        g[u].append((v, w))

    hp = []
    dist = [float("inf")] * n

    k = nxt()
    for _ in range(k):
        u = nxt() - 1
        dist[u] = 0
        heappush(hp, (0, u))

    while hp:
        d, u = heappop(hp)
        if d > dist[u]:
            continue
        if u == ed:
            print(d)
            return
        for v, w in g[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heappush(hp, (nd, v))

    print(-1)


if __name__ == "__main__":
    while True:
        try:
            solve()
        except StopIteration:
            break
