n = int(input())

ans = [[0] * n for _ in range(n)]

idx = 1
for i in range(n):
    for j in range(i, n):
        ans[i][j] = idx
        idx += 1

for i in range(1, n):
    for j in range(i):
        ans[i][j] = ans[j][i]

for row in ans:
    print(*row)