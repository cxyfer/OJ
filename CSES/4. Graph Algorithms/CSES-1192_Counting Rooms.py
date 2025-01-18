n, m = map(int, input().split())
grid = [list(input()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
DIR = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def dfs(x, y):
    st = [(x, y)]
    while st:
        x, y = st.pop()
        if x < 0 or x >= n or y < 0 or y >= m or grid[x][y] == "#" or visited[x][y]:
            continue
        visited[x][y] = True
        for dx, dy in DIR:
            st.append((x + dx, y + dy))

ans = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == "." and not visited[i][j]:
            dfs(i, j)
            ans += 1
print(ans)