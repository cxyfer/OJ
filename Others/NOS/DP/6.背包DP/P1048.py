"""
P1048 [NOIP 2005 普及组] 采药
https://www.luogu.com.cn/problem/P1048
背包DP模板題，求極值
"""
T, M = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(M)]

f = [0] * (T + 1)
for t, v in items:
    for j in range(T, t - 1, -1):
        f[j] = max(f[j], f[j - t] + v)

print(f[T])