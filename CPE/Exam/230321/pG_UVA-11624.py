"""
    BFS
    Simple version of Leetcode 2258. Escape the Spreading Fire

    UVA 只給 1s 的時間限制，Python 會 TLE，要改成 C++
    CPE 和 ZeroJudge 能 AC

    搶地盤
    Jack 能不能搶到邊緣的地盤
"""
import sys
input = sys.stdin.readline
def print(val=""): sys.stdout.write(str(val) + "\n")

from collections import deque

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    grid = [list(input().strip()) for _ in range(n)]

    q = deque() # (i, j, is_fire, time)
    vis = [[False] * m for _ in range(n)] # visited
    for i, row in enumerate(grid):
        for j, ch in enumerate(row):
            if ch == '.': continue
            if ch == 'F':
                q.append((i, j, True, 0))
            elif ch == 'J': # Joe
                st = (i, j, False, 0)
            vis[i][j] = True

    ans = -1
    q.append(st)
    while q:
        x, y, is_fire, time = q.popleft()
        if not is_fire and (x == 0 or x == n - 1 or y == 0 or y == m - 1):
            ans = time + 1 # Joe escape at next time
            break
        for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            if 0 <= nx < n and 0 <= ny < m and not vis[nx][ny]:
                vis[nx][ny] = True
                q.append((nx, ny, is_fire, time + 1))
    print(ans if ans != -1 else "IMPOSSIBLE")