"""
    區間DP
    dp[i][j][0/1]: 訪問區間 [i,j] 時所需時間，且最後一次訪問點在 i/j
    UVA 會 RE ，原因未知；CPE 用 Python 能 AC

    tags: DP, 區間DP, 紫書-Ch9, CPE-151006
    reference: https://blog.csdn.net/qq_37656398/article/details/81634469
"""
while True:
    try:
        n = int(input().strip())
    except EOFError:
        break
    a, b = [0] * n, [0] * n
    for i in range(n):
        a[i], b[i] = map(int, input().strip().split())
    dp = [[[0, 0] for _ in range(n)] for _ in range(n)]
    for i in range(n-1, -1, -1):
        for j in range(i+1, n):
            dp[i][j][0] = min(dp[i+1][j][0] + a[i+1] - a[i], dp[i+1][j][1] + a[j] - a[i])
            if dp[i][j][0] >= b[i]:
                dp[i][j][0] = float('inf')
            dp[i][j][1] = min(dp[i][j-1][0] + a[j] - a[i], dp[i][j-1][1] + a[j] - a[j-1])
            if dp[i][j][1] >= b[j]:
                dp[i][j][1] = float('inf')
    ans = min(dp[0][n-1][0], dp[0][n-1][1])
    print(ans if ans != float('inf') else 'No solution')
