import sys
input = sys.stdin.readline
def print(val=""): sys.stdout.write(str(val)+"\n")

MAX_MONEY = 7500
coins = [1, 5, 10, 25, 50]
dp = [1] + [0] * MAX_MONEY

for coin in coins:
    for i in range(coin, MAX_MONEY + 1):
        dp[i] += dp[i - coin]

while True:
    try:
        n = int(input())
    except:
        break
    print(dp[n])