n = int(input())
intervals = [list(map(int, input().split())) for _ in range(n)]

intervals.sort(key=lambda x: x[0])
merged = []
for l, r in intervals:
    if merged and merged[-1][1] >= l:
        merged[-1][1] = max(merged[-1][1], r)
    else:
        merged.append([l, r])

for l, r in merged:
    print(l, r)