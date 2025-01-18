from collections import defaultdict

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    cnt = defaultdict(int)
    for _ in range(k):
        b, c = map(int, input().split())
        cnt[str(b)] += c

    print(sum(sorted(cnt.values(), reverse=True)[:n]))