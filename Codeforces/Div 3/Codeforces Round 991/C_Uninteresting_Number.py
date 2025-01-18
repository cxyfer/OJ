MX = 180
t = int(input())

for _ in range(t):
    s = input()
    cnt = [0] * 10
    for ch in s:
        cnt[ord(ch) - ord('0')] += 1
    tot = sum(x * v for x, v in enumerate(cnt))
    if tot % 9 == 0:
        print("YES")
        continue
    f = [False] * (MX + 1)
    f[0] = True
    for x in [2, 3]:
        d = x * x - x 
        for _ in range(cnt[x]):
            for j in range(MX, d - 1, -1):
                if f[j - d]:
                    f[j] = True
    t = 9 - (tot % 9)
    while t <= MX and not f[t]:
        t += 9
    print("YES" if t <= MX else "NO")