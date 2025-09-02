import math
# Input
N = int(input())
checkpoints  = [list(map(int, input().split(" "))) for _ in range(N)] # coordinates of checkpoint i 

# DP

# dp[i][j] 表示前i+1個點中，跳過j個點的最短路徑
BOUND = min(N, 30)
dp = [[math.inf] * BOUND for _ in range(N)]
dp[0][0] = 0
for i in range(N):
    for j in range(BOUND):
        next_i = i + 1 + j # 找到下一個點，中間跳過j個點
        if next_i >= N:
            break
        distance = math.dist(checkpoints[i], checkpoints[next_i])
        # 跳過j個點的轉移方程：dp[i+j+1][k] = min(dp[i+j+1][k], dp[i][k-j] + distance)
        for k in range(j, BOUND): # 對k = [j, BOUND) 的範圍進行更新
            dp[next_i][k] = min(dp[next_i][k], dp[i][k-j] + distance)
ans = dp[N-1][0] # 跳過0個點的最短路徑，penalty = 0
for k in range(1, BOUND):
    ans = min(ans, dp[N-1][k] + 2**(k-1))
print(ans)