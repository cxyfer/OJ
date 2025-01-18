n = int(input())
times1, times2 = [], []
for _ in range(n):
    st, ed = map(int, input().split())
    times1.append(st)
    times2.append(ed)

times1.sort()
times2.sort()

i = j = 0
ans = cur = 0
while i < n and j < n:
    if i < n and times1[i] < times2[j]:
        cur += 1
        i += 1
    elif j < n and times1[i] > times2[j]:
        cur -= 1
        j += 1
    else:
        i += 1
        j += 1
    ans = max(ans, cur)

print(ans)