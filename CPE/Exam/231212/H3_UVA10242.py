from collections import *

while (True):
    try:
        P = list(map(float, input().split()))
        if len(P) != 8: # 看別人的程式碼，發現測資有空白行，媽的 = =
            break
    except:
        break

    cnt = Counter()
    for i in range(4):
        x, y = P[i * 2], P[i * 2 + 1]
        cnt[(x, y)] += 1
    x, y = 0, 0
    for (dx, dy), v in cnt.items():
        x += dx if v == 1 else -dx
        y += dy if v == 1 else -dy
    print(f"{x:.3f} {y:.3f}")