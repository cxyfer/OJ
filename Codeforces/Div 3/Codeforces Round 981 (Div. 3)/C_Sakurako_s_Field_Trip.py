"""
    貪心，在遇到會導致 disturbance 的情況時，交換對稱位置的值。
    最後計算還有多少對相鄰的值是相同的。
"""
t = int(input())

for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    
    for i in range(1, n // 2 + 1):
        if A[i] == A[i-1] or A[n-i-1] == A[n-i]:
            A[i], A[n-i-1] = A[n-i-1], A[i]
    print(sum(A[i] == A[i-1] for i in range(1, n)))