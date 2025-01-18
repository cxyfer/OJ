N, Q = map(int, input().split())
S = input()
S = list(S)
queries = [input().split() for _ in range(Q)]

# dp[i][j] 表示從i到j的字串 S[i:j+1] 是否為迴文
dp = [[False] * N for _ in range(N)] 
for i in range(N):
    dp[i][i] = True
for i in range(1, N-1):
    for k in range(1, N-i): # 距離
        if i - k < 0 or i + k >= N:
            break
        print(i-k, i+k)
        if S[i-k] == S[i+k]:
            dp[i-k][i+k] = True and dp[i-k][i+k]

for query in queries:
    q_type = int(query[0]) # 1 or 2
    if q_type == 1:
        x, ch = int(query[1])-1, query[2]
        S[x] = ch
        # Update dp
        for i in range(x+1, N):
            k = x - i
            if i - k < 0 or i + k >= N:
                break
            if S[i-k] == S[i+k]:
                dp[i-k][i+k] = True and dp[i-k][i+k]


    else:
        L, R = int(query[1])-1, int(query[2])-1
        if dp[L][R]:
            print("Yes")
        else:
            print("No")

