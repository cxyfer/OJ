from heapq import *

while True:
    L, R, C = map(int, input().split())
    if L == 0 and R == 0 and C == 0:
        break
    cube = []
    for _ in range(L):
        cube.append([input() for _ in range(R)])
        input()

    st, ed = (-1, -1, -1), (-1, -1, -1)
    for x in range(L):
        for y in range(R):
            for z in range(C):
                if cube[x][y][z] == 'S':
                    st = (x, y, z)
                elif cube[x][y][z] == 'E':
                    ed = (x, y, z)

    dist = [[[float('inf')] * C for _ in range(R)] for _ in range(L)]
    dist[st[0]][st[1]][st[2]] = 0

    hp = [(0, st)]
    while hp:
        d, (x, y, z) = heappop(hp)
        if (x, y, z) == ed:
            print(f'Escaped in {d} minute(s).')
            break
        if d > dist[x][y][z]:
            continue
        for dx, dy, dz in [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]:
            nx, ny, nz = x + dx, y + dy, z + dz
            if 0 <= nx < L and 0 <= ny < R and 0 <= nz < C:
                if cube[nx][ny][nz] == '#':
                    continue
                nd = d + 1
                if nd < dist[nx][ny][nz]:
                    dist[nx][ny][nz] = nd
                    heappush(hp, (nd, (nx, ny, nz)))
    else:
        print('Trapped!')