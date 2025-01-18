from collections import defaultdict

n = int(input())

cnt = defaultdict(int)

for _ in range(n):
    line = input()
    for ch in line:
        if ch.isalpha():
            cnt[ch.upper()] += 1

for k, v in sorted(cnt.items(), key = lambda x : (-x[1], x[0])):
    print(k, v)
