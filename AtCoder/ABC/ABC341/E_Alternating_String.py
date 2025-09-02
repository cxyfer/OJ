N, Q = map(int, input().split())
S = list(map(int, list(input())))
queries = [list(map(int, input().split())) for _ in range(Q)]

dp = [False] * N
dp[0] = True

for i in range(1, N):
    if S[i] != S[i-1]:
        dp[i] = dp[i-1]

for query in queries:
    t, l, r = query
    l -= 1
    r -= 1
    if t == 1:
        for i in range(l, r+1):
            S[i] = 1 if S[i] == 0 else 0
            if i > 0 and S[i] != S[i-1]:
                dp[i] = dp[i-1]
    else:
        print("Yes" if dp[r] else "No")

