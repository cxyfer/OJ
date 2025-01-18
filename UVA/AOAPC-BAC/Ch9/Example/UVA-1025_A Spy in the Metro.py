"""
    DP
    令 dp[t][i] 表示時間 t 在車站 i 的最少等待時間
"""
from functools import cache
kase = 1
TOP_DOWN_DP = True
while True:
    n = int(input())
    if n == 0:
        break
    T = int(input())
    dist = [0] + list(map(int, input().split()))
    M1 = int(input())
    arr1 = list(map(int, input().split()))
    M2 = int(input())
    arr2 = list(map(int, input().split()))

    # 預處理，令 has_train[t][i][0/1] 表示時刻t，在車站i是否有向右/左開的火車
    has_train = [[[False, False] for _ in range(n+1)] for _ in range(T+1)]
    for st in arr1: # 從第1站出發，由左往右
        for i in range(1, n):
            if st > T: # 到達第i站的時候已經超時了
                break
            has_train[st][i][0] = True
            st += dist[i]
    for st in arr2: # 從第n站出發，由右往左
        for i in range(n, 1, -1):
            if st > T:
                break
            has_train[st][i][1] = True
            st += dist[i-1]

    if TOP_DOWN_DP: # Top-down DP
        @cache
        def f(i, j):
            if i == T:
                return 0 if j == n else float('inf')
            res = f(i+1, j) + 1
            if j < n and has_train[i][j][0] and i+dist[j] <= T:
                res = min(res, f(i+dist[j], j+1))
            if j > 1 and has_train[i][j][1] and i+dist[j-1] <= T:
                res = min(res, f(i+dist[j-1], j-1))
            return res
        ans = f(0, 1)
    else: # Bottom-up DP
        dp = [[0] * (n+1) for _ in range(T+1)]
        dp[T][n] = 0 # 已經在終點站，不用等待
        for i in range(1, n): # 最終時刻不應該到達其他站
            dp[T][i] = float('inf')
        for i in range(T-1, -1, -1):
            for j in range(1, n+1):
                dp[i][j] = dp[i+1][j] + 1 # 等待一個時間單位
                if j < n and has_train[i][j][0] and i+dist[j] <= T: # 有火車可以往右，從時刻 i+dist[j] 到達第 j+1 站轉移
                    dp[i][j] = min(dp[i][j], dp[i+dist[j]][j+1])
                if j > 1 and has_train[i][j][1] and i+dist[j-1] <= T: # 有火車可以往左，從時刻 i+dist[j-1] 到達第 j-1 站轉移
                    dp[i][j] = min(dp[i][j], dp[i+dist[j-1]][j-1])
        ans = dp[0][1] # 時刻0從第1站出發所需的最少等待時間
        
    print(f'Case Number {kase}: {ans if ans != float("inf") else "impossible"}')
    kase += 1