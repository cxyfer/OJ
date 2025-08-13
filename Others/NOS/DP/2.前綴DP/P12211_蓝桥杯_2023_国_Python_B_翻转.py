import sys
sys.setrecursionlimit(int(2e5))
from functools import cache

n = int(input())
s = [input() for _ in range(n)]

@cache
def dfs(i, c):
    if i == n:
        return 0
    return min(dfs(i + 1, s[i][1]) + (1 if s[i][0] == c else 2),
              dfs(i + 1, s[i][0]) + (1 if s[i][1] == c else 2))

print(dfs(0, ''))