"""
    包含 A[i] 的子序列數量 = 2^(n-1)
    當 n > 1 時，答案必定是 0
    當 n == 1 時，答案是 A[0]
"""
n = int(input())
A = list(map(int, input().split()))

if n == 1:
    print(A[0])
else:
    print(0)