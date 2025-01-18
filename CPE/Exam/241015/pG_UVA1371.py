import sys
input = sys.stdin.readline
def print(val=""): sys.stdout.write(str(val) + "\n")

t = int(input())

for _ in range(t):
    x = input().strip()
    y = input().strip()

    def check(mid):
        # dp = [[0] * (len(y) + 1) for _ in range(len(x) + 1)]
        # for i in range(1, len(x) + 1):
        #     dp[i][0] = i
        # for j in range(1, len(y) + 1):
        #     dp[0][j] = j
        #     if dp[len(x)][j - 1] <= mid:
        #         dp[0][j - 1] = 0
        #     for i in range(1, len(x) + 1):
        #         dp[i][j] = min(dp[i - 1][j] + 1,
        #                        dp[i][j - 1] + 1,
        #                        dp[i - 1][j - 1] + (0 if x[i - 1] == y[j - 1] else 1))
        # return dp[len(x)][len(y)] <= mid
    
        dp = [[0] * (len(x) + 1) for _ in range(len(y) + 1)]
        for j in range(1, len(x) + 1):
            dp[0][j] = j
        for i in range(1, len(y) + 1):
            dp[i][0] = i
            if dp[i - 1][len(x)] <= mid:
                dp[i - 1][0] = 0
            for j in range(1, len(x) + 1):
                dp[i][j] = min(1 + dp[i - 1][j], 1 + dp[i][j - 1], dp[i - 1][j - 1] + (0 if x[j - 1] == y[i - 1] else 1))
        return dp[len(y)][len(x)] <= mid    

    left, right = 0, len(x)
    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            right = mid - 1
        else:
            left = mid + 1
    print(left)