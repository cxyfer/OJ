kase = 1
DIR = {'A': (-1, 0), 'B': (1, 0), 'L': (0, -1), 'R': (0, 1)}

while True:
    # input
    mp = [[] for _ in range(5)]
    line = input()
    if line == 'Z':
        break
    mp[0] = list(line)
    for i in range(1, 5):
        mp[i] = list(input())
    cmd = ""
    while True:
        s = input()
        cmd += s
        if s[-1] == '0':
            break
    # process
    if kase > 1:
        print()
    print(f"Puzzle #{kase}:")
    kase += 1
    x, y = 0, 0
    for i in range(5):
        for j in range(5):
            if mp[i][j] == ' ':
                x, y = i, j
                break
        if x and y:
            break
    flag = False # no final configuration
    cmd = cmd[:-1] # remove the last '0'
    for ch in cmd:
        if ch not in DIR: # invalid command
            flag = True
            break
        dx, dy = DIR[ch]
        nx, ny = x + dx, y + dy
        if 0 <= nx < 5 and 0 <= ny < 5:
            mp[x][y], mp[nx][ny] = mp[nx][ny], mp[x][y] # swap
            x, y = nx, ny
        else:
            flag = True
            break
    if flag:
        print("This puzzle has no final configuration.")
        continue
    else:
        for i in range(5):
            for j in range(5):
                print(mp[i][j], end=" " if j < 4 else "")
            print()

