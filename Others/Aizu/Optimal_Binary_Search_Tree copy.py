n = int(input())
P = list(map(float, input().split()))
Q = list(map(float, input().split()))

f = [[0 for _ in range(n+2)] for _ in range(n+2)]
w = [[0 for _ in range(n+2)] for _ in range(n+2)]
m = [[0 for _ in range(n+2)] for _ in range(n+2)]

# 初始情況：樹的高度為0時，期望成本為 q[i]
for i in range(n+1):
    f[i][i] = Q[i]
    w[i][i] = Q[i]
    m[i][i] = i

# 計算所有可能的區間長度
for ln in range(1, n+1):  # l 是區間的長度
    for i in range(n - ln + 1):
        j = i + ln
        f[i][j] = float('inf')
        w[i][j] = w[i][j-1] + P[j-1] + Q[j]
        for k in range(i, j):
            temp = f[i][k] + f[k+1][j] + w[i][j]
            if temp < f[i][j]:
                f[i][j] = temp
                m[i][j] = k
print(f"{f[0][n]:.8f}")