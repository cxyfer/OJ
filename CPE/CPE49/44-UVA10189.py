tc = 1
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    mp = [list(input().strip()) for _ in range(n)]
    if tc > 1:
        print()
    print(f"Field #{tc}:")
    tc += 1
    ans = [["0"] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if mp[i][j] == "*":
                ans[i][j] = "*"
                continue
            cnt = 0
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if 0 <= i + dx < n and 0 <= j + dy < m and mp[i + dx][j + dy] == "*":
                        cnt += 1
            ans[i][j] = str(cnt)
    for i in range(n):
        print("".join(ans[i]))