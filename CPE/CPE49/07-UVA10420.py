from collections import Counter

T = int(input())
cnt = Counter()

for _ in range(T):
    country, *name = input().split() # name 不一定是兩個字，用 *name 來接收剩下的字串
    cnt[country] += 1

for k, v in sorted(cnt.items()):
    print(k, v)