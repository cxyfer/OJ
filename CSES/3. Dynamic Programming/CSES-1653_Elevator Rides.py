"""
    狀壓DP
    Python 會 TLE，差一個測試點
"""
n, x = map(int, input().split())
W = list(map(int, input().split()))
W.sort()

# 預先計算每個狀態的重量
weights = [0] * (1 << n)
for i in range(n): # 初始化
    weights[1 << i] = W[i]
for i in range(1 << n): # 透過位運算消除最低位的 1 來計算重量
    weights[i] = weights[i - (i & -i)] + weights[i & -i]

u = (1 << n) - 1

# dp[i] = (rides, subset)，其中 i 是二進制表示的人員組合
dp = [(float('inf'), 0) for _ in range(1 << n)]
dp[0] = (1, 0)
for mask in range(1, 1 << n):
    for j in range(n):
        if mask & (1 << j):
            rides, s = dp[mask ^ (1 << j)]
            if weights[s | (1 << j)] > x:
                rides += 1
                s = (1 << j)
            else:
                s |= (1 << j)
            # 更新答案
            if rides < dp[mask][0]: # 次數更少 
                dp[mask] = (rides, s)
            elif rides == dp[mask][0] and weights[s] < weights[dp[mask][1]]: # 次數相同，但重量更小
                dp[mask] = (rides, s)
print(dp[u][0])