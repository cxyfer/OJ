from collections import Counter

N, K = map(int, input().split())
P = [list(map(int, input().split())) for _ in range(N)]

# 分開考慮 x, y 座標
cnt_x = Counter()
cnt_y = Counter()

for x, y in P:
    cnt_x[x] += 1
    cnt_y[y] += 1

max_x = max(cnt_x.keys())
min_x = min(cnt_x.keys())
max_y = max(cnt_y.keys())
min_y = min(cnt_y.keys())

d1 = max_x - min_x
d2 = max_y - min_y

ans = max(d1, d2)

if ans == 0:
    print(ans)
    exit()

# 嘗試在K次操作內縮小邊界

while (K > 0):
    d1 = max_x - min_x
    d2 = max_y - min_y
    if d1 == d2: # 縮小邊界
        mn = min(cnt_x[max_x], cnt_x[min_x], cnt_y[max_y], cnt_y[min_y])
        if mn > K:
            break
        if cnt_x[max_x] == mn:
            cnt_x[max_x] = 0
            while (cnt_x[max_x] == 0):
                max_x -= 1
        elif cnt_x[min_x] == mn:
            cnt_x[min_x] = 0
            while (cnt_x[min_x] == 0):
                min_x += 1
        elif cnt_y[max_y] == mn:
            cnt_y[max_y] = 0
            while (cnt_y[max_y] == 0):
                max_y -= 1
        elif cnt_y[min_y] == mn:
            cnt_y[min_y] = 0
            while (cnt_y[min_y] == 0):
                min_y += 1
        K -= mn
        ans = max(max_x - min_x, max_y - min_y)
    elif d1 > d2: # 縮小x邊界
        mn = min(cnt_x[max_x], cnt_x[min_x])
        if mn > K:
            break
        if cnt_x[max_x] == mn:
            cnt_x[max_x] = 0
            while (cnt_x[max_x] == 0):
                max_x -= 1
        elif cnt_x[min_x] == mn:
            cnt_x[min_x] = 0
            while (cnt_x[min_x] == 0):
                min_x += 1
        K -= mn
        ans = max(max_x - min_x, max_y - min_y)
    else: # 縮小y邊界
        mn = min(cnt_y[max_y], cnt_y[min_y])
        if mn > K:
            break
        if cnt_y[max_y] == mn:
            cnt_y[max_y] = 0
            while (cnt_y[max_y] == 0):
                max_y -= 1
        elif cnt_y[min_y] == mn:
            cnt_y[min_y] = 0
            while (cnt_y[min_y] == 0):
                min_y += 1
        K -= mn
        ans = max(max_x - min_x, max_y - min_y)
    print(ans, max_x, min_x, max_y, min_y, K)
    if ans == 0:
        break
print(ans)