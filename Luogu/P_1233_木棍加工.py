"""
    題目要求的是 把一個序列劃分成 **最少** 個非遞增子序列的數目。
    根據 Dilworth's theorem ，其等於這個序列的最長遞增子序列的長度(LIS)。
"""

n = int(input())

A = list(map(int, input().split()))
sticks = []
for i in range(n):
    sticks.append((A[2*i], A[2*i+1]))

sticks.sort(key=lambda x: (-x[0], -x[1]))
# print(sticks)

dp = [1] * n
for i in range(n):
    for j in range(i):
        if sticks[i][1] > sticks[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))