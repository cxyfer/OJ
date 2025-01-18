kase = 1
while True:
    line = input()
    if line == '0':
        break
    r, c = map(int, line.split())
    tbl = [list(input()) for _ in range(r)]
    mark = [[0] * c for _ in range(r)]
    idx = 1
    for i in range(r):
        for j in range(c):
            if tbl[i][j] != '*' and (i == 0 or j == 0 or tbl[i - 1][j] == '*' or tbl[i][j - 1] == '*'):
                mark[i][j] = idx
                idx += 1
    if kase > 1:
        print()
    print(f'puzzle #{kase}:')
    kase += 1
    print('Across')
    for i in range(r):
        for j in range(c):
            if tbl[i][j] != '*' and (j == 0 or tbl[i][j - 1] == '*'): # 開始位置
                cur = ""
                for k in range(j, c):
                    if tbl[i][k] == '*':
                        break
                    cur += tbl[i][k]
                print(f'{mark[i][j]:3d}.{cur}')
    print('Down')
    for i in range(r):
        for j in range(c):
            if tbl[i][j] != '*' and (i == 0 or tbl[i - 1][j] == '*'): # 開始位置
                cur = ""
                for k in range(i, r):
                    if tbl[k][j] == '*':
                        break
                    cur += tbl[k][j]
                print(f'{mark[i][j]:3d}.{cur}')
                