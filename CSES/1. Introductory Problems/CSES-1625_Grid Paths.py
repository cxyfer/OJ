""" CSES-1625 Grid Paths
    Backtracking

    完全暴力是 4 ^ 48 ，不管如何都會 TLE，必須剪枝：
    - 走過的格子不能再走
    - 走到邊界外
    - 提前走到終點
    - 把自己困在某個區域
        由於起點和終點都在邊界上，因此若上下走過但左右沒走過，或左右走過但上下沒走過，則會把圖分成兩部分，無法走到終點

    但就算剪枝，Python 還是會 TLE 了，必須用 C++ 寫
"""
N = 9
S = 48
cmd = input()

ans = 0
visited = [[False] * N for _ in range(N)]
for i in range(N): # padding
    visited[i][0] = visited[i][N-1] = visited[0][i] = visited[N-1][i] = True

def dfs(x, y, step):
    global ans
    if x <= 0 or x >= N-1 or y <= 0 or y >= N-1: # 越界
        return
    if visited[x][y]: # 走過
        return
    if x == 7 and y == 1: # 到達終點，檢查步數
        ans += 1 if step == S else 0
        return
    if step >= S: # 超過步數，不合法，但應該不會有這種情況
        return
    # 由於起點和終點都在邊界上，因此若上下走過但左右沒走過，或左右走過但上下沒走過，則會把圖分成兩部分，無法走到終點
    if visited[x-1][y] and visited[x+1][y] and not visited[x][y-1] and not visited[x][y+1]:
        return
    if not visited[x-1][y] and not visited[x+1][y] and visited[x][y-1] and visited[x][y+1]:
        return
    
    visited[x][y] = True
    if cmd[step] == "U":
        dfs(x-1, y, step+1)
    elif cmd[step] == "D":
        dfs(x+1, y, step+1)
    elif cmd[step] == "L":
        dfs(x, y-1, step+1)
    elif cmd[step] == "R":
        dfs(x, y+1, step+1)
    else:
        dfs(x-1, y, step+1)
        dfs(x+1, y, step+1)
        dfs(x, y-1, step+1)
        dfs(x, y+1, step+1)
    visited[x][y] = False

dfs(1, 1, 0)
print(ans)