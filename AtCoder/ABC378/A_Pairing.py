A = list(map(int, input().split()))
cnt = [0] * (5)
for x in A:
    cnt[x] += 1
print(sum(x // 2 for x in cnt))