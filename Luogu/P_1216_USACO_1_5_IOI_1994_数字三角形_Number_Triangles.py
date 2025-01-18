r = int(input())
rows = [list(map(int, input().split())) for _ in range(r)]

f = [[-1] * r for _ in range(r)]
f[0][0] = rows[0][0]
for i in range(1, r):
    for j in range(i + 1):
        f[i][j] = rows[i][j] + max(f[i - 1][j], f[i - 1][j - 1])
print(max(f[r - 1]))