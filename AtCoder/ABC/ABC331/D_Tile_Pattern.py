N, Q = map(int, input().split())

grid = [list(input()) for _ in range(N)]
quries = [list(map(int, input().split())) for _ in range(Q)]

# 計算二維前綴和
pre_sum = [[0]*(N+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, N+1):
        pre_sum[i][j] = (grid[i-1][j-1] == 'B') + pre_sum[i - 1][j] + pre_sum[i][j - 1] - pre_sum[i - 1][j - 1]

# 在無限重複的平面上，計算(0, 0)到(x, y)內的黑色格子數量
def f(x, y):
    res = (x // N) * (y // N) * pre_sum[N][N]
    res += pre_sum[x % N][y % N]
    res += pre_sum[x % N][N] * (y // N)
    res += pre_sum[N][y % N] * (x // N)
    return res

for (A, B, C, D) in quries:
    C += 1
    D += 1
    print(f(C, D) - f(A, D) - f(C, B) + f(A, B))