import sys
buf = sys.stdin.read().split()
cin = lambda: buf.pop(0)
def print(val=""): sys.stdout.write(str(val)+"\n")

while True:
    try:
        N = int(cin())
    except:
        break
    grid = [[int(cin()) for _ in range(N)] for _ in range(N)]

    ans = -float('inf')
    for i in range(N):
        col = [0] * N # row[k] = sum(grid[i][k] to grid[j][k])
        for j in range(i, N):
            for k in range(N):
                col[k] += grid[j][k]
            dp = [col[0]] + [0] * (N - 1) # 把問題一維化
            for k in range(1, N):
                dp[k] = max(col[k], dp[k - 1] + col[k]) # 和前面的部分組合 or 自己獨立
            ans = max(ans, max(dp))
    print(ans)