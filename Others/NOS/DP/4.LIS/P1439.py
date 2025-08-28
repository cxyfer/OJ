"""
P1439 【模板】最长公共子序列
https://www.luogu.com.cn/problem/P1439
二維 LIS

考慮 LCS 中的值 x 在 P, Q 中對應的下標 i, j，則長度為 k 的 LCS 需滿足：
- i_x1 < i_x2 < ... < i_xk
- j_x1 < j_x2 < ... < j_xk
且 P[i_x1] = Q[j_x1], P[i_x2] = Q[j_x2], ..., P[i_xk] = Q[j_xk]

故問題可以轉換成對兩個下標陣列求二維LIS。
且由於下標天然是有序的，所以可以直接固定一維，在求出另外一維的對應下標後求 LIS 即可。
"""
from bisect import bisect_left

n = int(input())
P = list(map(lambda x: int(x) - 1, input().split()))
Q = list(map(lambda x: int(x) - 1, input().split()))

mp = [0] * n
for i, x in enumerate(P):
    mp[x] = i

f = []
for i, y in enumerate(Q):
    idx = bisect_left(f, mp[y])
    if idx == len(f):
        f.append(mp[y])
    else:
        f[idx] = mp[y]
print(len(f))


# mp1, mp2 = [0] * n, [0] * n
# for i, p in enumerate(P):
#     mp1[p] = i
# for i, q in enumerate(Q):
#     mp2[q] = i
# pairs = [(mp1[i], mp2[i]) for i in range(n)]
# pairs.sort()

# f = []
# for i, (x, y) in enumerate(pairs):
#     idx = bisect_left(f, y)
#     if idx == len(f):
#         f.append(y)
#     else:
#         f[idx] = y
# print(len(f))