n = int(input())
intervals = [list(map(int, input().split())) for _ in range(n)]
intervals.sort()

merged = [intervals[0]]
for l, r in intervals[1:]:
    if l > merged[-1][1]:
        merged.append([l, r])
    else:
        merged[-1][1] = max(merged[-1][1], r)

ans1 = ans2 = 0
for i, (l, r) in enumerate(merged):
    ans1 = max(ans1, r - l)
    if i > 0:
        ans2 = max(ans2, l - merged[i - 1][1])
print(ans1, ans2)