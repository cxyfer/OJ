from collections import deque

n = int(input())

ans = [[-1] * n for _ in range(n)]
ans[0][0] = 0
q = deque([(0, 0)])
while q:
    x, y = q.popleft()
    for dx in range(-2, 3):
        for dy in range(-2, 3):
            if abs(dx) + abs(dy) != 3:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and ans[nx][ny] == -1:
                ans[nx][ny] = ans[x][y] + 1
                q.append((nx, ny))

for row in ans:
    print(*row)