from collections import Counter
 
M = int(input())
 
cnt = Counter()
 
for _ in range(M):
    t, v = map(int, input().split())
    if t == 1:
        cnt[v] += 1
    else:
        tmp = cnt.copy()
        d = 0
        flag = True
        while flag and (d < 30): # 由低位到高位檢查
            if v >> d & 1:
                if tmp[d] > 0:
                    tmp[d] -= 1
                else:
                    flag = False
                    break
                tmp[d+1] += tmp[d] // 2
            d += 1
        print('YES' if flag else 'NO')