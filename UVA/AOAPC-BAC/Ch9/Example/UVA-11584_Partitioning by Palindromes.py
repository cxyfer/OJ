"""
    DP：回文分割
    Python 在 UVA 會 TLE，需要用 C++
    ZeroJudge 需要開I/O優化才能過，但有點極限
    CPE 能直接過，但測資又双叒叕有不符合格式的情況了，還是暗資，不通靈根本發現不了
    tags: DP, 回文, 紫書, CPE-221213
"""

import sys
buf = sys.stdin.read().split()
cin = lambda: buf.pop(0)
def print(val):
    sys.stdout.write(str(val) + '\n')

# t = int(input())
t = int(cin())
for _ in range(t):
    # s = input()
    s = cin()
    n = len(s)
    is_palindrome = [[False] * n for _ in range(n)]
    for i in range(n):
        is_palindrome[i][i] = True
    for k in range(2, n+1): # k: 子字串長度
        for i in range(n-k+1):
            j = i + k - 1
            if k == 2:
                is_palindrome[i][j] = s[i] == s[j]
            else:
                is_palindrome[i][j] = s[i] == s[j] and is_palindrome[i+1][j-1]
    dp = [0] * (n+1) # dp[i]: s[0:i] 的最小分割次數
    for i in range(1, n+1):
        dp[i] = i
        for j in range(i):
            if is_palindrome[j][i-1]:
                dp[i] = min(dp[i], dp[j] + 1)
    print(dp[n])
