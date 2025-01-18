from collections import deque

H, W = map(int, input().split())
grid = [list(input()) for _ in range(H)]

st, ed = (-1, -1), (-1, -1)
for i in range(H):
    for j in range(W):
        if grid[i][j] == 'S':
            st = (i, j)
        elif grid[i][j] == 'G':
            ed = (i, j)

def bfs(st, ed, vertical=True):
    dist = [[float('inf')] * W for _ in range(H)]
    dist[st[0]][st[1]] = 0
    q = deque([(st[0], st[1], 0 if vertical else 1)])
    while q:
        x, y, flag = q.popleft()
        if (x, y) == ed:
            return dist[x][y]
        for dx, dy in ([(1, 0), (-1, 0)] if flag else [(0, 1), (0, -1)]):
            nx, ny = x + dx, y + dy
            if 0 <= nx < H and 0 <= ny < W:
                if grid[nx][ny] == '#':
                    continue
                nd = dist[x][y] + 1
                if nd < dist[nx][ny]:
                    dist[nx][ny] = nd
                    q.append((nx, ny, flag ^ 1))
    return float('inf')

ans = min(bfs(st, ed, True), bfs(st, ed, False))
print(ans if ans != float('inf') else -1)