from collections import Counter
t = int(input())

for kase in range(1, t+1):
    n, m = map(int, input().split())
    mp = [list(input().strip()) for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]
    def dfs(x, y, ch):
        if x < 0 or x >= n or y < 0 or y >= m or visited[x][y] or mp[x][y] != ch:
            return
        visited[x][y] = True
        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            dfs(x+dx, y+dy, ch)

    cnt = Counter()
    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                dfs(i, j, mp[i][j])
                cnt[mp[i][j]] += 1
    print(f"World #{kase}")
    for k, v in sorted(cnt.items(), key=lambda x: (-x[1], x[0])):
        print(f"{k}: {v}")
        