"""
[x, 2x) -> 1, [2x, 3x) -> 2, ..., [kx, (k+1)x-1] -> k
"""
from collections import Counter

n = int(input())
A = list(map(int, input().split()))

mx = max(A)
cnt = Counter(A)
s = [0] * (mx + 1)
for x in range(1, mx + 1):
    s[x] = s[x - 1] + cnt[x]

ans = 0
for x in range(1, mx + 1):
    if cnt[x] == 0:
        continue
    ans += cnt[x] * (cnt[x] - 1) // 2  # 自身的貢獻
    for k in range(1, mx // x + 1):
        l = x + 1 if k == 1 else k * x
        r = min(mx, (k + 1) * x - 1)
        ans += cnt[x] * k * (s[r] - s[l - 1])
print(ans)