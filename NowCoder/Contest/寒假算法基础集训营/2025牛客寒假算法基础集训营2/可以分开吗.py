from collections import deque

n, m = map(int, input().split())
grid = [input() for _ in range(n)]
vis = [[False] * m for _ in range(n)]

ans = float('inf')
for i, row in enumerate(grid):
    for j, ch in enumerate(row):
        if ch == '0' or vis[i][j]:
            continue
        vis[i][j] = True
        st = set()
        q = deque([(i, j)])
        while q:
            x, y = q.popleft()
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m:
                    if grid[nx][ny] == '1':
                        if not vis[nx][ny]:
                            vis[nx][ny] = True
                            q.append((nx, ny))
                    else:
                        st.add((nx, ny))
        ans = min(ans, len(st))

print(ans)