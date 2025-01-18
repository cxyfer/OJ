from collections import defaultdict
from heapq import *
t = int(input())

for _ in range(t):
    mp = [[0] * 7 for _ in range(7)]
    for i in range(7):
        s = input()
        for j in range(7):
            mp[i][j] = 1 if s[j] == 'B' else 0
    seen = set()
    cnt = defaultdict(set)
    for i in range(1, 6):
        for j in range(1, 6):
            if mp[i][j] == mp[i + 1][j + 1] == mp[i + 1][j - 1] == mp[i - 1][j + 1] == mp[i - 1][j - 1] == 1:
                seen.add((i, j))
                cnt[(i+1, j+1)].add((i, j))
                cnt[(i+1, j-1)].add((i, j))
                cnt[(i-1, j+1)].add((i, j))
                cnt[(i-1, j-1)].add((i, j))
    
    ans = 0
    while seen:
        mx, x, y = 0, 0, 0
        for k in cnt:
            size = len(cnt[k])
            if size > mx:
                mx = size
                x, y = k
        if mx > 1:
            for u, v in cnt[(x, y)]: # 將(x, y)改成W後可影響的(u, v)
                seen.remove((u, v)) 
                for xx, yy in [(u+1, v+1), (u+1, v-1), (u-1, v+1), (u-1, v-1)]:
                    if (xx, yy) != (x, y) and (xx, yy) in cnt and (u, v) in cnt[(xx, yy)]:
                        cnt[(xx, yy)].remove((u, v))
            del cnt[(x, y)]
            ans += 1
        else:
            ans += len(seen)
            break
    print(ans)
