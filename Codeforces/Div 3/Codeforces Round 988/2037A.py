from collections import defaultdict

t = int(input())

for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))

    cnt = defaultdict(int)
    for x in A:
        cnt[str(x)] += 1

    ans = 0
    for k, v in cnt.items():
        ans += v // 2
    print(ans)