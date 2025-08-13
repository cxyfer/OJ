N = int(input())
COLORS = 11
grid = [list(map(int, input().split())) for _ in range(N)]

def calc():
    res = 0
    f = [0] * N
    for c in range(COLORS):
        for row in grid:
            for i, x in enumerate(row):
                if x != c:
                    f[i] = 0
                else:
                    f[i] = min(f[i - 1] if i > 0 else 0, f[i]) + 1
            res = max(res, max(f))
    return res

ans = 0
for _ in range(4):
    ans = max(ans, calc())
    # 順時針旋轉 90 度
    for i in range(N):
        for j in range(i):
            grid[i][j], grid[j][i] = grid[j][i], grid[i][j]
    for row in grid:
        row.reverse()
print(ans)