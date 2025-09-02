N = int(input())
S = " " + input()
C = [0] + list(map(int, input().split()))

"""
    dp1[i][j] 表示將S[:i]變成01交錯，且以j結尾的最小花費
    dp2[i][j] 表示將S[i:]變成10交錯，且以j開頭的最小花費
"""
dp1 = [[0 for _ in range(2)] for _ in range(N + 2)]
dp2 = [[0 for _ in range(2)] for _ in range(N + 2)]

for i in range(1, N+1):
    for j in range(2):
        dp1[i][j] = dp1[i-1][j^1] + (S[i] != str(j)) * C[i]
for i in range(N, 0, -1):
    for j in range(2):
        dp2[i][j] = dp2[i+1][j^1] + (S[i] != str(j)) * C[i]

ans = float('inf')
for i in range(1, N):
    ans = min(ans, dp1[i][0] + dp2[i+1][0])
    ans = min(ans, dp1[i][1] + dp2[i+1][1])
print(ans)