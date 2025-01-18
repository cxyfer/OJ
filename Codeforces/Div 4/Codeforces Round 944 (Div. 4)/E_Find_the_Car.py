"""
    Binary Search
    疑似有精度問題，由於是直接捨入，所以可以對唯一的除法用整除
"""
from bisect import *

t = int(input())

for _ in range(t):
    n, k, q = map(int, input().split())
    A = [0] + list(map(int, input().split()))
    B = [0] + list(map(int, input().split()))
    ans = []
    for _ in range(q):
        x = int(input())
        i = bisect_left(A, x)
        if A[i] == x:
            ans.append(B[i])
        else:
            ans.append(B[i-1] + (x - A[i-1]) * (B[i] - B[i-1]) // (A[i] - A[i-1])) # 用整除
    print(*ans)
