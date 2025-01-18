from collections import deque

t = int(input())
input()

for kase in range(1, t + 1):
    if kase > 1:
        print()
    x, y = map(lambda x: int(x) - 1, input().split()) # 注意输入的坐标是1-indexed

    grid = []
    while True:
        try:
            line = input().strip()
        except EOFError:
            break
        if line == "":
            break
        grid.append(line)
    n, m = len(grid), len(grid[0])

    q = deque([(x, y)])
    vis = [[False] * m for _ in range(n)]
    vis[x][y] = True
    ans = 1
    while q:
        x, y = q.popleft()
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == '0' and not vis[nx][ny]:
                vis[nx][ny] = True
                q.append((nx, ny))
                ans += 1
    print(ans)