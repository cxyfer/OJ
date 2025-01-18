"""
    DP
    令 f(i, k) 表示高度為 i，且塔頂有 k 個 Block 的方案數
    - 當 k == 1 時，f(i, 1) = f(i - 1, 1) * 2 + f(i - 1, 2)
        - 有三種情況：
            1. 在高度為 i - 1 層且塔頂有 1 個 Block 的情況下，繼續放 1 個 1 x 2 的 Block
            2. 在高度為 i - 1 層且塔頂有 1 個 Block 的情況下，將塔頂的 Block 往上延伸
            3. 在高度為 i - 1 層且塔頂有 2 個 Block 的情況下，只能在塔頂放 1 個 1 x 2 的 Block
    - 當 k == 2 時，f(i, 2) = f(i - 1, 2) * 4 + f(i - 1, 1)
        - 有四種情況：
            1. 在高度為 i - 1 層且塔頂有 2 個 Block 的情況下，繼續放 2 個 1 x 1 的 Block
            2. 在高度為 i - 1 層且塔頂有 2 個 Block 的情況下，延伸其中一個 Block，另一個放置 1 x 1 的 Block
            3. 在高度為 i - 1 層且塔頂有 2 個 Block 的情況下，延伸兩個 Block
            4. 在高度為 i - 1 層且塔頂有 1 個 Block 的情況下，只能在塔頂放 2 個 1 x 1 的 Block
    - 初始條件：f(1, 1) = 1, f(1, 2) = 1
    - 答案：f(n, 1) + f(n, 2)
"""
MOD = int(1e9 + 7)
N = int(1e6 + 5)

dp = [[0] * 3 for _ in range(N)]
dp[1][1] = dp[1][2] = 1
for i in range(2, N):
    dp[i][1] = (dp[i - 1][1] * 2 + dp[i - 1][2]) % MOD
    dp[i][2] = (dp[i - 1][1] + dp[i - 1][2] * 4) % MOD
 
t = int(input())
for _ in range(t):
    n = int(input())
    print((dp[n][1] + dp[n][2]) % MOD)