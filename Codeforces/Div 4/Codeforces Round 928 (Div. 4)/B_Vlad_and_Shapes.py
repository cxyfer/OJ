t = int(input())

for _ in range(t):
    N = int(input())
    mp = [list(map(int, list(input()))) for _ in range(N)]
    
    flag = True
    cnt = 0
    for row in mp:
        if row.count(1):
            if not cnt:
                cnt = row.count(1)
            else:
                if cnt != row.count(1):
                    flag = False
                    break
    print('SQUARE' if flag else 'TRIANGLE')