n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

for x in range(n):
    for y in range(n):
        for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if grid[nx][ny] * grid[x][y] > 0:  # 都是正數或都是負數
                print("NO")
                exit()
print("YES")