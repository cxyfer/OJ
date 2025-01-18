"""
    Prefix Sum
"""
from math import isqrt

MAX_N = 1e5 + 10

arr = [0] * int(MAX_N)
s = 0
for i in range(1, isqrt(int(MAX_N)) + 1):
    arr[i * i] = 1
pre_sum = [0] * int(MAX_N)
for i in range(1, int(MAX_N)):
    pre_sum[i] = pre_sum[i - 1] + arr[i]
while True:
    L, R = map(int, input().split())
    if L == 0 and R == 0:
        break
    print(pre_sum[R] - pre_sum[L - 1])