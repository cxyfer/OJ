"""
P8776 [蓝桥杯 2022 省 A] 最长不下降子序列
https://www.luogu.com.cn/problem/P8776

為方便說明，以下的 LIS 指的是 Longest Non-decreasing Subsequence。

分成三段：
1. [0, i) 的 LIS ，但 LIS 的最後一個元素必須不能超過 A[i + k]
2. [i, i + k) ，把這段修改成 A[i + k]
3. [i + k, n) 的 LIS
"""
from bisect import bisect_right

n, k = map(int, input().split())
A = list(map(int, input().split()))

# 先求以 i 開始的 LIS 長度
f = []
suf = [0] * n
for i in range(n - 1, -1, -1):
    idx = bisect_right(f, -A[i])
    if idx == len(f):
        f.append(-A[i])
    else:
        f[idx] = -A[i]
    suf[i] = idx + 1

# 前後綴分解求答案
ans = 0
f = []
for i in range(n - k):
    # 在 [0, i) 中，且末尾元素不超過 A[i + k] 的 LIS 長度
    ln = bisect_right(f, A[i + k]) + 1
    ans = max(ans, ln + k + suf[i + k] - 1)
    # 維護 LIS
    idx = bisect_right(f, A[i])
    if idx == len(f):
        f.append(A[i])
    else:
        f[idx] = A[i]
print(ans)