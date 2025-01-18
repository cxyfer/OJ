"""
    DP 
    改成先枚舉硬幣，再枚舉金額，就能使同種硬幣先被處理，進而確保不重複。
    
    例如當 coins = [2, 5]，x = 9 時，先枚舉硬幣再枚舉金額會是：
    - 2
    - 2 + 2
    - 2 + 2 + 2
    - 2 + 2 + 2 + 2
    - 5
    - 2 + 5
    - 2 + 2 + 5 (o)
    但先枚舉金額再枚舉硬幣會是：
    - 2
    - 2 + 2
    - 5
    - 2 + 2 + 2
    - 5 + 2
    - 2 + 5
    - 2 + 2 + 2 + 2
    - 5 + 2 + 2 (o)
    - 2 + 5 + 2 (o)
    - 2 + 2 + 5 (o)
"""
n, x = map(int, input().split())
coins = list(map(int, input().split()))
MOD = int(1e9 + 7)

dp = [0] * (x + 1)
dp[0] = 1
for c in coins:
    for i in range(c, x + 1):
        dp[i] += dp[i - c]
        dp[i] %= MOD
print(dp[x])