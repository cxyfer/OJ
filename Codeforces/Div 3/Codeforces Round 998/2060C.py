from collections import defaultdict

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    A = list(map(int, input().split()))

    a = b = 0
    cnt = defaultdict(int)
    for x in A:
        if cnt[str(k - x)] > 0:
            cnt[str(k - x)] -= 1
            a += 2
        else:
            cnt[str(x)] += 1
    b = n - a
    print((a - 1) // 2 if b & 1 else a // 2)