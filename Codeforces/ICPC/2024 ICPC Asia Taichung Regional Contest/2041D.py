from collections import deque

n, m = map(int, input().split())
grid = [input() for _ in range(n)]

st_x = st_y = ed_x = ed_y = -1
for nd, row in enumerate(grid):
    for j, val in enumerate(row):
        if val == 'S':
            st_x, st_y = nd, j
        elif val == 'T':
            ed_x, ed_y = nd, j

DIR = [(0, 1), (1, 0), (0, -1), (-1, 0)]
vis = set()
vis.add((st_x, st_y, -1, 0))
q = deque([(0, st_x, st_y, -1, 0)]) # time, x, y, dir, cnt
while q:
    t, x, y, d, cnt = q.popleft()
    if x == ed_x and y == ed_y:
        exit(print(t))
    for nd, (dx, dy) in enumerate(DIR):
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] != '#':
            nt = t + 1
            ncnt = cnt + 1 if nd == d else 1
            if ncnt > 3:
                continue
            state = (nx, ny, nd, ncnt)
            if state not in vis:
                vis.add(state)
                q.append((nt, nx, ny, nd, ncnt))
print(-1)