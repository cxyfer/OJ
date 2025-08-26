"""
P1020 [NOIP 1999 提高组] 导弹拦截
https://www.luogu.com.cn/problem/P1020

第一問：求最長非嚴格遞減子序列長度
- 1. 直接逆過來求最長非嚴格遞增子序列
- 2. 用負數
第二問：求最長嚴格遞增子序列長度
"""
from bisect import bisect_left, bisect_right

A = list(map(int, input().split()))
n = len(A)

f = []
for x in A[::-1]:
    idx = bisect_right(f, x)
    if idx == len(f):
        f.append(x)
    else:
        f[idx] = x
print(len(f))

f = []
for x in A:
    idx = bisect_left(f, x)
    if idx == len(f):
        f.append(x)
    else:
        f[idx] = x
print(len(f))