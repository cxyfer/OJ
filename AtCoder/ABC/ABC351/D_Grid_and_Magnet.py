"""
    題意要求的自由度，其實就是最大的連通分量大小
"""
from functools import cache
import sys
sys.setrecursionlimit(10**6)

H, W = map(int, input().split())
mp = [list(input()) for _ in range(H)]
check = [[False] * W for _ in range(H)] # 周圍是否有磁鐵

for i in range(H):
    for j in range(W):
        if mp[i][j] == '#':
            for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= ni < H and 0 <= nj < W:
                    check[ni][nj] = True
def dfs(x, y):
    if visited[x][y]: # 已經走過
        return 0
    if not check[x][y]: # 周圍有磁鐵，檢查是否已經標記過
        if (x, y) not in st:
            st.add((x, y))
            return 1
        return 0
    visited[x][y] = True
    res = 1
    for nx, ny in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
        if 0 <= nx < H and 0 <= ny < W and mp[nx][ny] == '.' and not visited[nx][ny]:
            res += dfs(nx, ny)
    return res

ans = 1
visited = [[False] * W for _ in range(H)]
for i in range(H):
    for j in range(W):
        if mp[i][j] == '#' or visited[i][j] or not check[i][j]:
            continue
        st = set()
        ans = max(ans, dfs(i, j))
print(ans)