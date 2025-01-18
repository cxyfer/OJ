"""
    前綴和 + 二分

    有一堆的前綴和轉換
"""
from bisect import *

n = int(input())
A = [-1] + list(map(int, input().split()))

# ps[i] = A[1] + A[2] + ... + A[i] 表示前 i 項的和
ps = [0] * (n + 1)
for i in range(1, n + 1):
    ps[i] = ps[i - 1] + A[i]

# pss[i] = s(1, 1) + s(1, 2) + ... + s(1, i) 表示在第 1 橫列中，前 i 項的和，前綴和的前綴和
pss = [0] * (n + 1)
for i in range(1, n + 1):
    pss[i] = pss[i - 1] + ps[i]

# f[i] = s(i, i) + s(i, i + 1) + ... + s(i, n) 表示第 i 橫列的和
f = [0] * (n + 1)
f[n] = A[n]
for i in range(n - 1, 0, -1):
    f[i] = f[i + 1] + A[i] * (n - i + 1)

# psr[i] = f[1] + f[2] + ... + f[i] 表示前 i 橫列的和
psr = [0] * (n + 1)
for i in range(1, n + 1):
    psr[i] = psr[i - 1] + f[i]

# sz[i] 表示前 i 橫列的元素個數，之後二分定位使用
sz = [0] * (n + 1)
for i in range(1, n + 1):
    sz[i] = sz[i - 1] + (n - i + 1)

# rowsum(i, j) = s(i, i) + s(i, i + 1) + ... + s(i, j)
# 此外，rowsum(i, n) = f[i]
def rowsum(i, j):
    return pss[j] - pss[i - 1] - ps[i - 1] * (j - i + 1)

def get(x):
    if x == 0:
        return 0
    i = bisect_left(sz, x)
    j = x - sz[i - 1]
    # 用 psr[i - 1] 求前 i - 1 橫列，接著求 s(i, i) + s(i, i + 1) + ... + s(i, i + j - 1) 這 j 個元素的和
    return psr[i - 1] + rowsum(i, i + j - 1)

q = int(input())
for _ in range(q):
    l, r = map(int, input().split())
    print(get(r) - get(l - 1))

# for i in range(1, n + 1):
#     for j in range(i, n + 1):
#         print(f"s({i}, {j}): ", get_rowsum(i, j))