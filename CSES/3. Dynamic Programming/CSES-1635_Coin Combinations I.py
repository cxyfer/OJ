"""
    DP
    Python 用填表法會 TLE，要用刷表法；C++ 則是兩種都可以
"""
n, x = map(int, input().split())
coins = list(map(int, input().split()))
coins.sort() # 這裡排序是為了剪枝
MOD = int(1e9 + 7)

dp = [0] * (x + 1)
dp[0] = 1
# 填表會 TLE
# for i in range(x + 1):
#     for c in coins:
#         if i - c < 0:
#             break
#         dp[i] += dp[i - c]
#         dp[i] %= MOD
for i in range(x + 1):
    for c in coins:
        if i + c > x: # 剪枝
            break
        dp[i + c] += dp[i]
        dp[i + c] %= MOD
print(dp[x])