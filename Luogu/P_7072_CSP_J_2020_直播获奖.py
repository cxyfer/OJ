MX = 600

n, w = map(int, input().split())
A = list(map(int, input().split()))

ans = []
cnt = [0] * (MX + 1)
for i, x in enumerate(A):
    cnt[x] += 1
    s = 0
    tgt = max(1, (i + 1) * w // 100)
    for j in range(MX, -1, -1):
        s += cnt[j]
        if s >= tgt:
            ans.append(j)
            break
print(*ans)