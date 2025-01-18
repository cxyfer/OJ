"""
令 [0, cur] 表示可以被構造出來的數字區間
則 [0, cur] 加上 coin 後可以構造出 [coin, cur + coin]
若兩個區間能拼接在一起，則表示能構造出 [0, cur + coin] 的數字

Similar questions:
- 1798. Maximum Number of Consecutive Values You Can Make
- 330. Patching Array
- 2952. Minimum Number of Coins to be Added
"""

n = int(input())
coins = list(map(int, input().split()))
coins.sort()

cur = 0
for coin in coins:
    if coin - cur > 1:  # 兩個區間不能拼接在一起
        break
    cur += coin

print(cur + 1)