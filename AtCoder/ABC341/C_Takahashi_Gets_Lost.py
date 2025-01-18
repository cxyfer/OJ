H, W, N = map(int, input().split())
S = input()
MAP = [list(input()) for _ in range(H)]
DICT = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

ans = 0
for i in range(1, H-1):
    for j in range(1, W-1):
        if MAP[i][j] == '#':
            continue
        x, y = i, j
        flag = True
        for dir in S:
            dx, dy = DICT[dir]
            x += dx
            y += dy
            if MAP[x][y] == '#':
                flag = False
                break
        if flag:
            ans += 1
print(ans)