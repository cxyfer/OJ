"""
    Dijkstra
    tags: CPE-140325

    UVA 和 CPE 上都會 TLE ，只能用 C++
"""
import sys
def input(): return sys.stdin.readline().strip()
def print(val=""): sys.stdout.write(str(val) + '\n')
from heapq import *

t = int(input())

for _ in range(t):
    n = int(input())
    m = int(input())
    mp = [list(map(int, input().split())) for _ in range(n)]
    dist = [[float('inf')] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    dist[0][0] = mp[0][0]
    hp = [(dist[0][0], 0, 0)]
    cnt = 0
    while hp:
        w, x, y = heappop(hp)
        if visited[x][y]: # 這個點已經被確定最短路徑了
            continue
        visited[x][y] = True # 確定這點的最短路徑
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                dist[nx][ny] = min(dist[nx][ny], w + mp[nx][ny])
                heappush(hp, (dist[nx][ny], nx, ny))
    print(dist[n - 1][m - 1])