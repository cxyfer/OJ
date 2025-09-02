H, W = map(int, input().split())
grid = [input() for _ in range(H)]

u, d = H + 1, -1
l, r = W + 1, -1
for i in range(H):
    for j in range(W):
        if grid[i][j] == '#':
            u = min(u, i)
            d = max(d, i)
            l = min(l, j)
            r = max(r, j)

if all(grid[i][j] != '.' for i in range(u, d + 1) for j in range(l, r + 1)):
    print("Yes")
else:
    print("No")