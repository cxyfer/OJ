t = int(input())

for _ in range(t):
    n = int(input())
    ans, mx = 0, 0
    for x in range(2, n+1): # 枚舉所有可能的 x
        k = n // x
        cur = (x + k * x) * (k + 1) // 2
        if cur > mx:
            mx = cur
            ans = x
    print(ans)