MAX_N = 30005
dollars = [5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]

dp = [0] * MAX_N
dp[0] = 1
for d in dollars:
    for i in range(d, MAX_N):
        dp[i] += dp[i - d]
        
while True:
    # n = float(input())
    a, b = map(int, input().split(".")) # 有精度問題，所以用整數來處理
    # if n == 0.00:
    if a == 0 and b == 0:
        break
    # print(f"{n:>6.2f}", end="")
    print(f"{a:3d}.{b:02d}", end="")
    n = a * 100 + b
    print(f"{dp[n]:17d}")
