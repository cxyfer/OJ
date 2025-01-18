from collections import deque

n, m = map(int, input().split())
grid = [list(input()) for _ in range(n)]
for i in range(n):
    for j in range(m):
        if grid[i][j] == "A":
            st = (i, j)
        elif grid[i][j] == "B":
            ed = (i, j)

DIR = [(1, 0, "D"), (-1, 0, "U"), (0, 1, "R"), (0, -1, "L")]

vis = [[False] * m for _ in range(n)]
dir = [[""] * m for _ in range(n)]
pre = [[(-1, -1)] * m for _ in range(n)]

q = deque([st])
while q:
    x, y = q.popleft()
    if (x, y) == ed:
        print("YES")
        ans = []
        while (x, y) != st:
            ans.append(dir[x][y])
            x, y = pre[x][y]
        ans.reverse()
        print(len(ans))
        print("".join(ans))
        break
    for dx, dy, ch in DIR:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= m or grid[nx][ny] == "#" or vis[nx][ny]:
            continue
        vis[nx][ny] = True
        pre[nx][ny] = (x, y)
        dir[nx][ny] = ch
        q.append((nx, ny))
else:
    print("NO")