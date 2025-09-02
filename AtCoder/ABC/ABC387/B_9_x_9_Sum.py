from collections import defaultdict

X = int(input())
tot = 0
cnt = defaultdict(int)
for i in range(1, 10):
    for j in range(1, 10):
        cnt[i * j] += 1
        tot += i * j
print(tot - X * cnt[X])