from collections import *

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    s = input()
    grid = [list(map(int, input().split())) for _ in range(n)]
    
    path = []
    i, j = 0, 0
    path.append((i, j))
    for ch in s:
        if ch == 'D':
            i += 1
        else:
            j += 1
        path.append((i, j))
    
    is_path = [[False] * m for _ in range(n)]
    for (i, j) in path:
        is_path[i][j] = True
    
    s_row = [0] * n
    s_col = [0] * m
    for i in range(n):
        for j in range(m):
            if is_path[i][j]:
                continue
            s_row[i] += grid[i][j]
            s_col[j] += grid[i][j]
    
    tgt_row = [-s_row[row] for row in range(n)]
    tgt_col = [-s_col[col] for col in range(m)]
    
    g_row = [[] for _ in range(n)]
    g_col = [[] for _ in range(m)]
    for (i, j) in path:
        g_row[i].append((i, j))
        g_col[j].append((i, j))
    
    q = deque()
    for i in range(n):
        if len(g_row[i]) == 1:
            q.append((0, i))
    for j in range(m):
        if len(g_col[j]) == 1:
            q.append((1, j))
    
    vis = set()
    while q:
        typ, idx = q.popleft()
        if typ == 0:
            if len(g_row[idx]) != 1:
                continue
            (i, j) = g_row[idx][0]
            if (i, j) in vis:
                continue
            vis.add((i, j))
            grid[i][j] = tgt_row[i]
            tgt_col[j] -= tgt_row[i]
            g_row[i].pop(0)
            g_col[j].remove((i, j))
            if len(g_col[j]) == 1:
                q.append((1, j))
        else:
            if len(g_col[idx]) != 1:
                continue
            (i, j) = g_col[idx][0]
            if (i, j) in vis:
                continue
            vis.add((i, j))
            grid[i][j] = tgt_col[j]
            tgt_row[i] -= tgt_col[j]
            g_col[j].pop(0)
            g_row[i].remove((i, j))
            if len(g_row[i]) == 1:
                q.append((0, i))

    # def check():
    #     row_sum = [sum(grid[i]) for i in range(n)]
    #     col_sum = [sum(grid[i][j] for i in range(n)) for j in range(m)]

    #     flag1 = all(row_sum[i] == row_sum[0] for i in range(n))
    #     flag2 = all(col_sum[j] == col_sum[0] for j in range(m))
    #     return flag1 and flag2 and row_sum[0] == col_sum[0]
    # print("YES" if check() else "NO")

    for row in grid:
        print(*row)