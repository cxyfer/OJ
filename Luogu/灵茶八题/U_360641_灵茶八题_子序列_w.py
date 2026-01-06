"""
U360641 灵茶八题 - 子序列 ^w^
https://www.luogu.com.cn/problem/U360641

和 +w+ 相同，包含 A[i] 的子序列數量有 2^(n-1) 個
當 n > 1 時，由於 2^(n-1) 是偶數，所以答案必定是 0
當 n == 1 時，答案是 A[0]
"""
n = int(input())
A = list(map(int, input().split()))

if n == 1:
    print(A[0])
else:
    print(0)