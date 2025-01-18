from collections import defaultdict

MOD = 100000000
M, N = map(int, input().split())  
grid = [list(map(int, input().split())) for _ in range(M)]

# 將地圖轉換為二進制表示，g[i] 表示第 i 行狀態，1 表示不能種植、0 表示可以種植
g = [0] * (M + 1)
for i in range(M):
    for j in range(N):
        g[i + 1] |= ((grid[i][j] == 0) << j)

# 生成所有合法狀態
states = []
for s in range(1 << N):
    if not (s & (s << 1)): # 需要至少間隔一格
        states.append(s)

# dp[i][s] 表示前 i 橫列，當前行狀態為 s 的方案數
prev = defaultdict(int)
prev[0] = 1
for i in range(1, M + 1):  
    curr = defaultdict(int)
    for s1 in states:
        if g[i] & s1:
            continue
        for s2 in states:
            if g[i - 1] & s2 or s1 & s2:
                continue
            curr[s1] = (curr[s1] + prev[s2]) % MOD
    prev = curr.copy()

# 計算最後一橫列所有可能狀態的總和
print(sum(curr.values()) % MOD)