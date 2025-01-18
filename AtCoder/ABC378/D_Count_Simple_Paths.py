"""
    Backtracking
    因為 K 最多只有 11，所以暴力搜索的計算量 H*W*4*3^10 是可以接受的
"""
import sys
sys.setrecursionlimit(10 ** 6)

H, W, K = map(int, input().split())
grid = [input().strip() for _ in range(H)]
DIR = [(-1,0), (1,0), (0,-1), (0,1)]

ans = 0
visited = [[False for _ in range(W)] for _ in range(H)]
def dfs(x, y, step):
    global ans
    if step == K:
        ans += 1
        return
    for dx, dy in DIR:
        nx, ny = x + dx, y + dy
        if 0 <= nx < H and 0 <= ny < W:
            if grid[nx][ny] == '.' and not visited[nx][ny]:
                visited[nx][ny] = True
                dfs(nx, ny, step + 1)
                visited[nx][ny] = False

for i in range(H):
    for j in range(W):
        if grid[i][j] == '.':
            visited[i][j] = True
            dfs(i, j, 0)
            visited[i][j] = False

print(ans)