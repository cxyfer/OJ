n, m = map(int, input().strip().split())

mp = [list(input().strip()) for _ in range(n)]

ans = [['*'] * m for _ in range(n)]

for x in range(n):
    for y in range(m):
        if mp[x][y] == '*':
            continue
        cnt = 0
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if 0 <= x + dx < n and 0 <= y + dy < m and mp[x + dx][y + dy] == "*":
                    cnt += 1
        ans[x][y] = cnt

for row in ans:
    print(*row, sep="")