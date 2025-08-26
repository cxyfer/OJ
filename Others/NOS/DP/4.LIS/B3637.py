"""
B3637 最长上升子序列
https://www.luogu.com.cn/problem/B3637
"""
from bisect import bisect_left

n = int(input())
A = list(map(int, input().split()))

f = []
for x in A:
    idx = bisect_left(f, x)
    if idx == len(f):
        f.append(x)
    else:
        f[idx] = x
print(len(f))