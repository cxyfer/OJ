"""
為了讓 Python 不會 TLE，需要盡可能將資訊紀錄在原本的 grid 上
"""

from collections import deque

n, m = map(int, input().split())

grid = [list(input()) for _ in range(n)]
DIR = [(0, 1, "R"), (0, -1, "L"), (1, 0, "D"), (-1, 0, "U")]

q = deque()
for x in range(n):
    for y in range(m):
        if grid[x][y] == "A":
            q.append((x, y, 0))
        elif grid[x][y] == "M":
            q.appendleft((x, y, 1))

while q:
    x, y, flag = q.popleft()
    if flag == 0 and (x == 0 or x == n - 1 or y == 0 or y == m - 1):
        print("YES")
        ans = []
        while grid[x][y] != "A":
            ans.append(grid[x][y])
            if grid[x][y] == "R":
                y -= 1
            elif grid[x][y] == "L":
                y += 1
            elif grid[x][y] == "D":
                x -= 1
            else:
                x += 1
        ans.reverse()
        print(len(ans))
        print("".join(ans))
        exit()
    for dx, dy, dir in DIR:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == ".":
            grid[nx][ny] = dir
            q.append((nx, ny, flag))
else:
    print("NO")