"""
    Backtracking

    AC: UVA, CPE, ZeroJudge
    ZeroJudge 上 Python 會 TLE，開輸出入優化也沒用
"""
ans = []
path = []
def dfs(x):
    if x == 1 and len(path) > 1:
        ans.append(path[:])
        return
    pre = path[-1] if path else 2 # 前一個數字
    for y in range(pre, x+1):
        if x % y == 0:
            path.append(y)
            dfs(x//y)
            path.pop()

while True:
    n = int(input())
    if n == 0:
        break
    ans.clear()
    dfs(n)
    print(len(ans))
    for a in ans:
        print(" ".join(map(str, a)))