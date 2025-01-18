N = int(input())
As = list(map(int, input().split(" ")))

dic = {}
for idx, A in enumerate(As):
    if A in dic:
        dic[A].append(idx)
    else:
        dic[A] = [idx]
ans = 0
for key, idxs in dic.items():
    if len(idxs) == 1:
        continue
    left = 0
    right = 1
    n = len(idxs)
    for i in range(n-1):
        ans += idxs[-1] - idxs[i] - (n-1-i-1)
        print(key, idxs, idxs[-1] - idxs[i], (n-1-i-1), idxs[-1] - idxs[i] - (n-1-i-1))
print(ans)
