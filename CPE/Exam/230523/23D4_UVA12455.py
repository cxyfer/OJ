"""
    類題：
    - 322. Coin Change
    - 416. Partition Equal Subset Sum
"""

T = int(input())

for _ in range(T):
    target = int(input())
    n = int(input())
    bars = list(map(int, input().split()))

    dp = [0] * (target + 1)
    dp = [False] * (target + 1)
    dp[0] = True
    for bar in bars:
        for i in range(target, bar - 1, -1):
            dp[i] |= dp[i - bar]

    print("YES" if dp[target] else "NO")