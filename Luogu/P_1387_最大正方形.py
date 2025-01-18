from functools import cache

n, m = map(int, input().split())
M = [list(map(int, input().split())) for _ in range(n)]

@cache
def dfs(i, j):
    if i >= n or j >= m:
        return 0
    if M[i][j] != 1:
        return 0
    return 1 + min(dfs(i + 1, j), dfs(i, j + 1), dfs(i + 1, j + 1))

ans = 0
for i in range(n):
    for j in range(m):
        ans = max(ans, dfs(i, j))
print(ans)