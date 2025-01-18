from collections import Counter
T = int(input())

for tc in range(1, T+1):
    mp = [list(input()) for _ in range(3)]
    for i, row in enumerate(mp):
        for j, ch in enumerate(row):
            if ch == '?':
                cnt = Counter(row)
                if cnt['A'] == 0:
                    print('A')
                elif cnt['B'] == 0:
                    print('B')
                else:
                    print('C')
                break
            
                
