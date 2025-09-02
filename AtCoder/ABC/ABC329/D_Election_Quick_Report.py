from collections import Counter

N, M = map(int, input().split())
A = list(map(int, input().split()))

cnt = Counter()
ans = 0
for a in A:
    cnt[a] += 1
    if cnt[a] > cnt[ans] or (cnt[a] == cnt[ans] and a < ans):
        ans = a
    print(ans)
    