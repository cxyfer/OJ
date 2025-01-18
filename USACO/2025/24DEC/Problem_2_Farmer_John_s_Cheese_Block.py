n, q = map(int, input().split())

cnt_x = [[0] * n for _ in range(n)]
cnt_y = [[0] * n for _ in range(n)]
cnt_z = [[0] * n for _ in range(n)]

ans = 0
for _ in range(q):
    x, y, z = map(int, input().split())

    cnt_x[y][z] += 1
    if cnt_x[y][z] == n:
        ans += 1
    cnt_y[x][z] += 1
    if cnt_y[x][z] == n:
        ans += 1
    cnt_z[x][y] += 1
    if cnt_z[x][y] == n:
        ans += 1

    print(ans)