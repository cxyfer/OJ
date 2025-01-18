"""
    Dynamic Programming
"""

T = int(input())

for _ in range(T):
    N = int(input())
    A = [0] + list(map(int, input().split()))

    # dp[i] 表示 以 a_i 結尾的最大子陣列和
    dp = [0] * (N+1)
    dp[1] = A[1]
    for i in range(2, N+1):
        if A[i-1] % 2 != A[i] % 2: # 奇偶性不同
            dp[i] = max(dp[i-1] + A[i], A[i])
        else: # 奇偶性相同
            dp[i] = A[i]
    print(max(dp[1:]))
