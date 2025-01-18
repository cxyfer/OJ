from itertools import accumulate

OUTPUT_DATAFRAME = False

n = int(input())
P = [0] + list(map(float, input().split())) #     k1, k2, ..., kn
Q = list(map(float, input().split()))       # d0, d1, d2, ..., dn

"""
令 T[i][j] 表示包含 k_i 到 k_j 的 OBST，且定義 T[i][i-1] 為空樹，則
- f[i][j] 表示此 OBST 的期望成本
- w[i][j] 表示此 OBST 的累積機率
  - w[i][j] = Sum(P[k] for k in range(i, j+1)) + Sum(Q[k] for k in range(i-1, j+1))
            = w[i][j-1] + p[j] + q[j]
- m[i][j] 表示此 OBST 的根位置，即最佳的分割點
"""
f = [[0 for _ in range(n+2)] for _ in range(n+2)]
w = [[0 for _ in range(n+2)] for _ in range(n+2)]
m = [[0 for _ in range(n+2)] for _ in range(n+2)]

# 初始化 f[i][i-1] = q[i-1]（空樹的期望成本）
for i in range(1, n+2):
    f[i][i-1] = Q[i-1]
    w[i][i-1] = Q[i-1]
    m[i][i-1] = i  # 根的位置初始化為 i

# 計算累積機率
# sp = list(accumulate(P, initial=0))
# sq = list(accumulate(Q, initial=0))
# def w(i, j):
#     return sp[j+1] - sp[i] + sq[j+1] - sq[i-1]
for i in range(1, n+1):
    for j in range(i, n+1):
        w[i][j] = w[i][j-1] + P[j] + Q[j]

# 動態規劃計算 f[i][j]
for ln in range(1, n + 1):  # 子樹的大小，這裡只考慮 k 的數量
    for i in range(1, n - ln + 2):
        j = i + ln - 1
        f[i][j] = float('inf')
        for k in range(i, j + 1):
            cost = f[i][k-1] + f[k+1][j] + w[i][j]
            if cost < f[i][j]:
                f[i][j] = cost
                m[i][j] = k
print(f"{f[1][n]:.8f}")

if OUTPUT_DATAFRAME:
    import numpy as np
    import pandas as pd

    f_df = pd.DataFrame(np.array(f[1:n+2])[:, 0:n+1], 
                    index=range(1, n+2), 
                    columns=range(0, n+1))
    w_df = pd.DataFrame(np.array(w[1:n+2])[:, 0:n+1], 
                    index=range(1, n+2), 
                    columns=range(0, n+1))
    m_df = pd.DataFrame(np.array(m[1:n+2])[:, 0:n+1], 
                    index=range(1, n+2), 
                    columns=range(0, n+1))

    print("\nExpected Cost Matrix (f):")
    print(f_df)
    print("\nAccumulated Probability Matrix (w):")
    print(w_df)
    print("\nRoot Position Matrix (m):")
    print(m_df)