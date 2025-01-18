t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    grid = [input() for _ in range(n)]

    ans = 0
    for k in range(min(n, m) // 2): # layer
        # 獲取第 k 層的遍歷字串
        s = ""
        for j in range(k, m - k): # 上
            s += grid[k][j]
        for i in range(k + 1, n - 1 -k): # 右
            s += grid[i][m - 1 -k]
        if n - 1 - k != k: # 下
            for j in range(m - 1 - k, k - 1, -1):
                s += grid[n - 1 - k][j]
        for i in range(n - 2 - k, k, -1): # 左
            s += grid[i][k]
        # 計算第 k 層的 1543 循環子字串數量
        sz = len(s)
        s = s + s[:4]
        for i in range(sz):
            if s[i:i+4] == '1543':
                ans += 1
    print(ans)