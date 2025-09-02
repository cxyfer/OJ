"""
    Prefix Sum
"""
from itertools import accumulate

N, Q = map(int, input().split())
S = input()
LR = [ list(map(int, input().split())) for _ in range(Q) ]

res = [0] * (N)
for i in range(1, N):
    if S[i] == S[i-1]:
        res[i] = 1

prefix_sum = list(accumulate(res))
# print(res)
# print(prefix_sum)
for l, r in LR:
    print(prefix_sum[r-1] - prefix_sum[l-1])