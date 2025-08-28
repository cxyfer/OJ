"""
P4303 [AHOI2006] 基因匹配
https://www.luogu.com.cn/problem/P4303
二維 LIS

和 P1439 類似，但每個值會有 5 個對應下標，
轉移時需要從大到小枚舉下標，否則從小到大會導致錯誤結果
"""
from bisect import bisect_left

n = int(input())
P = list(map(lambda x: int(x) - 1, input().split()))
Q = list(map(lambda x: int(x) - 1, input().split()))

pos = [[] for _ in range(n)]
for i, x in enumerate(P):
    pos[x].append(i)
for x in range(n):
    pos[x].reverse()

f = []
for j, y in enumerate(Q):
    for i in pos[y]:
        idx = bisect_left(f, i)
        if idx == len(f):
            f.append(i)
        else:
            f[idx] = i
print(len(f))