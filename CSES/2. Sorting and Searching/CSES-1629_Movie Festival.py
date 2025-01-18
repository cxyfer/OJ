n = int(input())
intervals = []
for _ in range(n):
    st, ed = map(int, input().split())
    intervals.append((st, ed))

intervals.sort(key=lambda x: x[1])

ans = last = 0
for st, ed in intervals:
    if st >= last:
        ans += 1
        last = ed

print(ans)