from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

lst = defaultdict(list)

for i, x in enumerate(A, start=1):
    lst[x].append(i)

mx = idx = -1
for x, idxs in lst.items():
    if len(idxs) > 1:
        continue
    if x > mx:
        mx = x
        idx = idxs[0]

print(-1 if mx == -1 else idx)