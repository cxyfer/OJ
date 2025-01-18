from collections import Counter
cnt = Counter()
N = int(input())
for _ in range(N):
    W, X = map(int, input().split())
    cnt[X] += W
ans = 0
for t in range(24):
    ans = max(ans, sum(cnt[x] for x in range(t, t+9)))
print(ans)