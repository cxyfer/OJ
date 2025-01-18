"""
    DP
    Python 有可能會 TLE，要看運氣
    uDebug上的測資是有問題的，被騙了
"""
import sys
from functools import *

input = sys.stdin.readline
def print(val=""): sys.stdout.write(str(val) + "\n")
sys.setrecursionlimit(10000)

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    A = [list(map(int, input().split())) for _ in range(n)] # 只能由右往左走
    B = [list(map(int, input().split())) for _ in range(n)] # 只能由下往上走
    sumA = [[0] * (m + 1) for _ in range(n + 1)] 
    sumB = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            sumA[i][j] = sumA[i][j - 1] + A[i - 1][j - 1]
            sumB[i][j] = sumB[i - 1][j] + B[i - 1][j - 1]
    # dp = [[0] * (m + 1) for _ in range(n + 1)] # Bottom-Up
    # for i in range(1, n + 1): # 注意，這裡的 i, j 是從 1 開始的
    #     for j in range(1, m + 1):
    #         res1 = dp[i - 1][j] + sumA[i][j] # 取這格在A中的值，即往左走，代表左邊的也能取到
    #         res2 = dp[i][j - 1] + sumB[i][j] # 取這格在B中的值，即往上走，代表上面的也能取到
    #         dp[i][j] = max(res1, res2)
    # print(dp[n][m]) 

    @cache
    def f(x, y): # 注意，這裡的 x, y 是從 1 開始的
        if x == 0 or y == 0:
            return 0
        res1 = f(x - 1, y) + sumA[x][y] # 取這格在A中的值，即往左走，代表左邊的也能取到
        res2 = f(x, y - 1) + sumB[x][y] # 取這格在B中的值，即往上走，代表上面的也能取到
        return max(res1, res2)
    print(f(n, m))