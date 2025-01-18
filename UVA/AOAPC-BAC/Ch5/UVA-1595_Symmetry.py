from collections import defaultdict

t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    points = []
    for _ in range(n):
        x, y = map(int, input().strip().split())
        points.append((x, y))

    cnt = defaultdict(lambda: defaultdict(int))
    for x, y in points:
        cnt[x][y] += 1

    x_keys = sorted(cnt.keys())
    m = len(x_keys)
    if m & 1:
        x_mid = x_keys[m // 2]
    else:
        x_mid = (x_keys[m // 2 - 1] + x_keys[m // 2]) / 2

    for x in x_keys:
        if cnt[x] != cnt[x_mid * 2 - x]:
            print("NO")
            break
    else:
        print("YES")