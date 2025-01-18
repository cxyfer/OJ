from functools import *

@cache
def dfs(n):
    if n == 1:
        return 1
    if n & 1:
        return dfs(3*n+1) + 1
    else:
        return dfs(n//2) + 1

while True:
    try:
        a, b = map(int, input().split())
    except EOFError:
        break
    
    ans = max(map(dfs, range(min(a, b), max(a,b)+1)))
    print(a, b, ans)