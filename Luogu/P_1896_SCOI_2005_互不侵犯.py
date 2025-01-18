from collections import defaultdict

N, K = map(int, input().split())

# 預先生成橫列的合法狀態
states = []
for s in range(1 << N):
    if (s & (s << 1)) == 0:
        states.append(s)

# 預處理相容狀態
compatible = defaultdict(list)
for prev in states:
    for curr in states:
        if not (((prev << 1) | prev | (prev >> 1)) & curr):
            compatible[prev].append(curr)

# dp[i][prev][k] 表示當前考慮到第 i 橫列，前一橫列的狀態為 prev ，已放置 k 個國王的方案數
# dp = [[[0] * (K + 1) for _ in range(1 << N)] for _ in range(N + 1)]
# dp[0][0][0] = 1

prev = defaultdict(lambda: defaultdict(int))
prev[0][0] = 1
for i in range(N):
    curr = defaultdict(lambda: defaultdict(int))
    for s1 in states:  # 枚舉當前橫列的狀態
        cnt = s1.bit_count()  # 當前狀態的國王數
        for k in range(K - cnt + 1):  # 枚舉已放置的國王數，確保總國王數不超過 K
            for s2 in compatible[s1]:  # 從前一橫列與當前橫列相容的狀態轉移
                curr[s1][k + cnt] += prev[s2][k]
    prev = curr.copy()

# 答案為考慮到第 N 行所有合法狀態中放置了 K 個國王的方案數
print(sum(curr[s][K] for s in states))
