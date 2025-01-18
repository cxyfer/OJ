""" CSES 1624 - Chessboard and Queens
    Backtracking
"""
n = 8
mp = [input() for _ in range(n)]
path = [0] * n #  row-i 的 Q 在 col-path[i]

ans = 0
def check(x, y): 
    for i in range(x): # 檢查前 x row
        j = path[i]
        if (x+y) == (i+j) or (x-y) == (i-j): # 位在同一條斜線上 (斜率相同)
            return False
    return True

def dfs(r, avail):
    global ans
    if r == n:
        ans += 1
        return
    for c in avail:
        if mp[r][c] == "." and check(r, c):
            path[r] = c
            dfs(r+1, avail-{c})
dfs(0, set(range(n)))
print(ans)